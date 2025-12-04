import os
import json
import pandas as pd


with open("games.json", "r", encoding="utf-8") as f:
        dataset = json.load(f)


rows = []

for app_id, game in dataset.items():

    row = {
        "app_id": app_id,
        "name": game.get("name"),
        "release_date": game.get("release_date"),
        "estimated_owners": game.get("estimated_owners"),
        "peak_ccu": game.get("peak_ccu"),
        "required_age": game.get("required_age"),
        "price": game.get("price"),
        "dlc_count": game.get("dlc_count"),
        "detailed_description": game.get("detailed_description"),
        "short_description": game.get("short_description"),
        "supported_languages": game.get("supported_languages"),
        "full_audio_languages": game.get("full_audio_languages"),
        "reviews": game.get("reviews"),
        "header_image": game.get("header_image"),
        "website": game.get("website"),
        "support_url": game.get("support_url"),
        "support_email": game.get("support_email"),
        "windows": game.get("windows"),
        "mac": game.get("mac"),
        "linux": game.get("linux"),
        "metacritic_score": game.get("metacritic_score"),
        "metacritic_url": game.get("metacritic_url"),
        "user_score": game.get("user_score"),
        "positive": game.get("positive"),
        "negative": game.get("negative"),
        "score_rank": game.get("score_rank"),
        "achievements": game.get("achievements"),
        "recommendations": game.get("recommendations"),
        "notes": game.get("notes"),
        "average_playtime": game.get("average_playtime_forever"),
        "average_playtime_2weeks": game.get("average_playtime_2weeks"),
        "median_playtime": game.get("median_playtime_forever"),
        "median_playtime_2weeks": game.get("median_playtime_2weeks"),
        "developers": ", ".join(game.get("developers", [])),
        "publishers": ", ".join(game.get("publishers", [])),
        "categories": ", ".join(game.get("categories", [])),
        "genres": ", ".join(game.get("genres", [])),
        "tags": ", ".join(game.get("tags", [])),
    }

    row["screenshots"] = ", ".join(game.get("screenshots", []))
    row["movies"] = ", ".join(game.get("movies", []))

    rows.append(row)


df = pd.DataFrame(rows)
df.to_csv("steam_games.csv", index=False)
