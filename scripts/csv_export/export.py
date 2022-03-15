#!/usr/bin/env python3
# coding: utf-8
#
# This script takes one or more paths as argument
# and exports all .pgn files into a single .csv file.
#
# Usage: python export.py first/path second\path third/*

import csv
from datetime import datetime
import os
import sys

import pgn


def collect_paths(path: str) -> list[str]:
    """Collects all subfolder paths inside a given folder
    if the given path ends with a star."""
    if path.endswith("*"):
        return list(x[0] for x in os.walk(path[:-1]))
    return [path]


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
            "duration": pgn_game.headers["Duration"],
            "seed": pgn_game.headers["Seed"],
            "depth_white": pgn_game.headers["Depth"].split("-")[0],
            "depth_black": pgn_game.headers["Depth"].split("-")[1],
            "total_cache_hits_white": pgn_game.headers["CacheHits"].split("-")[0],
            "total_cache_hits_black": pgn_game.headers["CacheHits"].split("-")[1],
            "state_changes": {
                node.comment: node.ply() for node in pgn_game.mainline() if node.comment
            },
            "total_moves": pgn_game.end().ply(),
            "filename": filename,
        }

        # Save results (uses white player name as key)
        games.append(results)
    return games


def export_to_csv(games: list[dict]) -> None:
    """Exports the given results dictionary to csv."""
    filename = f'statistics_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}.csv'
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        # Write headlines
        csv_writer.writerow(
            [
                "Player",
                "Result white",
                "Depth white",
                "Cache hits white",
                "Opponent",
                "Result black",
                "Depth black",
                "Cache hits black",
                "Outcome",
                "Moves",
                "Duration",
                "Moves to middle game",
                "Moves to end game",
                "Round",
                "Seed",
                "File",
            ]
        )
        # Write results
        for game in sorted(games, key=lambda game: game["filename"]):
            csv_writer.writerow(
                [
                    game["player"],
                    game["result_white"],
                    game["depth_white"],
                    game["total_cache_hits_white"],
                    game["opponent"],
                    game["result_black"],
                    game["depth_black"],
                    game["total_cache_hits_black"],
                    game["outcome"].split(".")[1],
                    game["total_moves"],
                    game["duration"].split(".")[0],
                    game["state_changes"].get("State.MIDDLE_GAME", "-"),
                    game["state_changes"].get("State.END_GAME", "-"),
                    game["round"].replace("/", " of "),
                    game["seed"],
                    game["filename"],
                ]
            )
    print(f"Exported {len(games)} games to '{filename}'")


# Run and export games
if __name__ == "__main__":
    folders = [full_path for path in sys.argv[1:] for full_path in collect_paths(path)]
    results = [game for folder in folders for game in collect_results(folder)]
    if results:
        export_to_csv(results)
    else:
        print(f"No .pgn files found in '{'; '.join(folders)}'")
