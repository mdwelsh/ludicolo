# Ludicolo!

This is a collection of scripts used to collect data from
https://pokemontcg.io/ for AI model training.

## Instructions

1. Clone this repository on github.
2. Run `poetry install` in this directory.
3. To gather image data, run:
```
poetry run python ludicolo/fetch_images.py
```
This will dump the image and caption data to the `images/` folder.

