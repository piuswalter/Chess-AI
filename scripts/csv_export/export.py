#!/usr/bin/env python3
# coding: utf-8
#
# This script takes one or more paths as argument
# and exports all .pgn files into a single .csv file.
#
# Usage: python export.py first/path second\path third/*

import csv
import json
import os
import sys
from datetime import datetime

import chess.pgn as pgn


def collect_paths(path: str) -> list[str]:
    """Collects all subfolder paths inside a given folder
    if the given path ends with a star."""
    if path.endswith("*"):
        return list(x[0] for x in os.walk(path[:-1]))
    return [path]


import chess.pgn as pgn


def generate_stats(nodes: pgn.Mainline[pgn.ChildNode]) -> dict:
    """Collects and generates stats from .pgn file comments"""
    # Prepare data
    stats = {}
    raw_stats: list[dict] = [json.loads("{" + node.comment + "}") for node in nodes]
    raw_stats_white = [raw_stats[i] for i in range(0, len(raw_stats), 2)]
    raw_stats_black = [raw_stats[i] for i in range(1, len(raw_stats), 2)]
    # Get stockfish elo and time limit
    for node in raw_stats:
        if "elo" in node:
            stats["elo"] = node["elo"]
            stats["time_limit"] = node["time_limit"]
            break
    # Get last game state
    stats["last_state"] = raw_stats[-2]["state"].split(".")[1]
    # Get total calculation time
    engine_time_white = sum(node["time"] for node in raw_stats_white)
    engine_time_black = sum(node["time"] for node in raw_stats_black)
    # Get average move calculation time
    stats["move_time_white"] = engine_time_white / len(raw_stats_white)
    stats["move_time_black"] = engine_time_black / len(raw_stats_black)
    # Get average depth of all moves (if applicable)
    depth_list_white = [
        node["avg_depth"] for node in raw_stats_white if "avg_depth" in node
    ]
    depth_list_black = [
        node["avg_depth"] for node in raw_stats_black if "avg_depth" in node
    ]
    stats["average_depth_white"] = sum(depth_list_white) / (len(depth_list_white) or 1)
    stats["average_depth_black"] = sum(depth_list_black) / (len(depth_list_black) or 1)
    # Get max depth of all moves (if applicable)
    max_depth_list_black = [
        node["max_depth"] for node in raw_stats_black if "max_depth" in node
    ]
    max_depth_list_white = [
        node["max_depth"] for node in raw_stats_white if "max_depth" in node
    ]
    stats["max_depth_white"] = (
        max(max_depth_list_white) if max_depth_list_white else "-"
    )
    stats["max_depth_black"] = (
        max(max_depth_list_black) if max_depth_list_black else "-"
    )
    # Get the percentage of overall cache hits
    cache_tries_white = sum(
        node["cache_tries"] for node in raw_stats_white if "cache_tries" in node
    )
    cache_tries_black = sum(
        node["cache_tries"] for node in raw_stats_black if "cache_tries" in node
    )
    cache_hits_white = sum(
        node["cache_hits"] for node in raw_stats_white if "cache_hits" in node
    )
    cache_hits_black = sum(
        node["cache_hits"] for node in raw_stats_black if "cache_hits" in node
    )
    stats["cache_hits_white"] = (
        cache_hits_white / cache_tries_white if cache_tries_white else "-"
    )
    stats["cache_hits_black"] = (
        cache_hits_black / cache_tries_black if cache_tries_black else "-"
    )
    # Get the maximum cache size (if applicable)
    cache_list_white = [
        node["cache_size_mb"] for node in raw_stats_white if "cache_size_mb" in node
    ]
    cache_list_black = [
        node["cache_size_mb"] for node in raw_stats_black if "cache_size_mb" in node
    ]
    stats["max_cache_size_mb_white"] = (
        max(cache_list_white) if cache_list_white else "-"
    )
    stats["max_cache_size_mb_black"] = (
        max(cache_list_black) if cache_list_black else "-"
    )
    # Get the complete list of moves
    stats["move_list"] = ",".join(entry["move"] for entry in raw_stats)
    # Get the complete list of visited nodes per move
    stats["nodes_list"] = ",".join(str(entry.get("nodes", 0)) for entry in raw_stats)
    return stats


# Collect results from .pgn files


def collect_results(folder: str) -> list[dict]:
    """Scans all .pgn files inside the games folder and collects the game results as dictionary."""
    # All results are presented from the view of the white color
    results_map_white = {"1-0": "Won", "0-1": "Lost", "1/2-1/2": "Remis", "*": "Remis"}
    results_map_black = {"0-1": "Won", "1-0": "Lost", "1/2-1/2": "Remis", "*": "Remis"}
    games: list[dict] = []

    # Iterate over all .pgn files
    for filename in os.listdir(folder):
        if not filename.endswith(".pgn"):
            continue
        with open(os.path.join(folder, filename)) as pgn_file:
            pgn_game = pgn.read_game(pgn_file)
        if not pgn_game:
            continue

        # Collect results
        results = {
            "round": pgn_game.headers["Round"],
            "player": pgn_game.headers["White"],
            "opponent": pgn_game.headers["Black"],
            "result_white": results_map_white[pgn_game.headers["Result"]],
            "result_black": results_map_black[pgn_game.headers["Result"]],
            "outcome": pgn_game.headers["Outcome"],
            "duration": float(pgn_game.headers["Duration"]),
            "seed": pgn_game.headers["Seed"],
            "commit": pgn_game.headers["Commit"],
            "depth_white": pgn_game.headers["Depth"].split("-")[0],
            "depth_black": pgn_game.headers["Depth"].split("-")[1],
            "total_moves": pgn_game.end().ply(),
            "filename": filename,
            **generate_stats(pgn_game.mainline()),
        }

        # Save results
        games.append(results)
    return games


import csv
from datetime import datetime


def export_to_csv(games: list[dict], target_folder: str) -> None:
    """Exports the given results dictionary to csv."""
    filename = f'statistics_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.csv'
    path = os.path.join(target_folder, filename)
    with open(path, "w", newline="") as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        # Write headlines
        csv_writer.writerow(
            [
                "Player",
                "Result white",
                "Depth white",
                "Average depth white",
                "Max depth white",
                "Average move time white (s)",
                "Cache hits white (%)",
                "Max cache size white (mb)",
                "Opponent",
                "Result black",
                "Depth black",
                "Average depth black",
                "Max depth black",
                "Average move time black (s)",
                "Cache hits black (%)",
                "Max cache size black (mb)",
                "Outcome",
                "Moves",
                "Duration (s)",
                "Last state",
                "Round",
                "Seed",
                "Commit Hash",
                "File",
                "Move list (uci)",
                "Nodes per move list",
                "Comment",
            ]
        )
        # Write results
        for game in sorted(games, key=lambda game: game["filename"]):
            for key in game:
                if isinstance(game[key], float):
                    game[key] = str(round(game[key], 2)).replace(".", ",")
            csv_writer.writerow(
                [
                    game["player"],
                    game["result_white"],
                    game["depth_white"],
                    game["average_depth_white"],
                    game["max_depth_white"],
                    game["move_time_white"],
                    game["cache_hits_white"],
                    game["max_cache_size_mb_white"],
                    game["opponent"],
                    game["result_black"],
                    game["depth_black"],
                    game["average_depth_black"],
                    game["max_depth_black"],
                    game["move_time_black"],
                    game["cache_hits_black"],
                    game["max_cache_size_mb_black"],
                    game["outcome"].split(".")[1],
                    game["total_moves"],
                    game["duration"],
                    game["last_state"],
                    game["round"].replace("/", " of "),
                    game["seed"],
                    game["commit"],
                    game["filename"],
                    game["move_list"],
                    game["nodes_list"],
                    ""
                    if "elo" not in game
                    else f'elo: {game["elo"]}, time_limit: {game["time_limit"]}',
                ]
            )
    print(f"Exported {len(games)} games to '{path}'")


# Run and export games
if __name__ == "__main__":
    folders = [full_path for path in sys.argv[1:] for full_path in collect_paths(path)]
    results = [game for folder in folders for game in collect_results(folder)]
    if results:
        export_to_csv(results, "./")
    else:
        print(f"No .pgn files found in '{'; '.join(folders)}'")
