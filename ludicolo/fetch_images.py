#!/usr/bin/env python3


import json
import os
import requests

BASE_URL = "https://raw.githubusercontent.com/PokemonTCG/pokemon-tcg-data/refs/heads/master/cards/en/base1.json"


def fetch_image(url: str, output_file: str):
    response = requests.get(url)
    response.raise_for_status()
    image_data = response.content
    with open(output_file, "wb") as f:
        f.write(image_data)
        print(f"Fetched {output_file}")


# Example data for one card:
# {
#     "id": "base1-1",
#     "name": "Alakazam",
#     "supertype": "Pokémon",
#     "subtypes": [
#       "Stage 2"
#     ],
#     "level": "42",
#     "hp": "80",
#     "types": [
#       "Psychic"
#     ],
#     "evolvesFrom": "Kadabra",
#     "abilities": [
#       {
#         "name": "Damage Swap",
#         "text": "As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pokémon to another as long as you don't Knock Out that Pokémon. This power can't be used if Alakazam is Asleep, Confused, or Paralyzed.",
#         "type": "Pokémon Power"
#       }
#     ],
#     "attacks": [
#       {
#         "name": "Confuse Ray",
#         "cost": [
#           "Psychic",
#           "Psychic",
#           "Psychic"
#         ],
#         "convertedEnergyCost": 3,
#         "damage": "30",
#         "text": "Flip a coin. If heads, the Defending Pokémon is now Confused."
#       }
#     ],
#     "weaknesses": [
#       {
#         "type": "Psychic",
#         "value": "×2"
#       }
#     ],
#     "retreatCost": [
#       "Colorless",
#       "Colorless",
#       "Colorless"
#     ],
#     "convertedRetreatCost": 3,
#     "number": "1",
#     "artist": "Ken Sugimori",
#     "rarity": "Rare Holo",
#     "flavorText": "Its brain can outperform a supercomputer. Its intelligence quotient is said to be 5000.",
#     "nationalPokedexNumbers": [
#       65
#     ],
#     "legalities": {
#       "unlimited": "Legal"
#     },
#     "images": {
#       "small": "https://images.pokemontcg.io/base1/1.png",
#       "large": "https://images.pokemontcg.io/base1/1_hires.png"
#     }
#   },


def write_caption(card: dict, output_file: str):
    prompt = (
        f"A TOK image of a {card['name']} Pokémon card. This is a "
        + f"{' '.join(card['types'])}-type Pokémon with {card['hp']} HP. "
        + f"The description is: {card['flavorText']}"
    )
    print(prompt)
    with open(output_file, "w") as f:
        f.write(prompt)


def fetch_card_image(card: dict):
    if "id" in card and "images" in card and "large" in card["images"]:
        fetch_image(card["images"]["large"], f"images/{card['id']}.png")
        write_caption(card, f"images/{card['id']}.txt")
    else:
        print(f"No image found for {card['id']}")


def main():
    os.makedirs("images", exist_ok=True)
    response = requests.get(BASE_URL)
    response.raise_for_status()
    data = json.loads(response.text)
    for card in data:
        if card.get("supertype") == "Pokémon":
            fetch_card_image(card)


if __name__ == "__main__":
    main()
