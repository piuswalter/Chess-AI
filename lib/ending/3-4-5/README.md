# Direkter Download

[ZIP-Datei hier herunterladen](https://plagemann.sharepoint.com/:u:/g/Ed63qeMQRf9Bk1XtSAEklEABDNHUFFCs__mpTICl1uDBBA?e=AcOQu5)

# Anleitung

Downloaden und Entpacken in den Ordner `3-4-5`.

# Befehl zum Download der Originaldateien
```sh
wget --execute="robots = off" --mirror --convert-links --no-parent http://tablebase.sesse.net/syzygy/3-4-5/
```

# Validierung

```sh
md5sum -c checksum.md5
```
