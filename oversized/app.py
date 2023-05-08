"""
This module contains the Flask app for the Oversized music artist page. The app is designed to be minimalistic, simple,
and responsive, and it retrieves artist information from a JSON file.

The app includes the following routes:

- /: The home page of the website. Displays the artist’s information retrieved from the artist.json file.

The app also includes static files (such as CSS and JavaScript) and HTML templates, which are located in the "static"
and "templates" directories, respectively.

To run the app, execute this file with Python:

    $ python app.py

By default, the app will be available at http://localhost:5000/ in your web browser.
"""

import datetime
from pathlib import Path
from typing import Any, Dict, Tuple

from flask import Flask, json, render_template

APP: Flask = Flask(__name__)

STATIC_FOLDER: Path = Path("oversized/static")

SOCIAL_MEDIAS: Dict[str, Tuple[str, str]] = {
    "facebook": ("Facebook", "https://www.facebook.com/<user>"),
    "instagram": ("Instagram", "https://www.instagram.com/<user>"),
    "twitter": ("Twitter", "https://twitter.com/<user>"),
    "tiktok": ("TikTok", "https://www.tiktok.com/@<user>"),
    "youtube": ("YouTube", "https://www.youtube.com/@<user>"),
    "twitch": ("Twitch", "https://www.twitch.com/<user>"),
    "soundcloud": ("SoundCloud", "https://www.soundcloud.com/<user>"),
}


def _check_personal_and_music_information(artist_data: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    for info_type in ["personal_information", "music_information"]:
        if info_type not in artist_data:
            continue

        for key, value in artist_data[info_type].items():
            if isinstance(value, str):
                try:
                    date = datetime.datetime.strptime(value, "%Y-%m-%d")
                    artist_data[info_type][key] = date.strftime("%x")
                except ValueError:
                    continue
            elif isinstance(value, list):
                joined_value = ", ".join(str(item) for item in value if isinstance(item, str))  # type: ignore
                if joined_value:
                    artist_data[info_type][key] = joined_value

    return artist_data


def _check_social_media(artist_data: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    if "social_media" not in artist_data:
        return artist_data

    social_media = {
        SOCIAL_MEDIAS[platform][0]: SOCIAL_MEDIAS[platform][1].replace("<user>", user)
        for platform, user in artist_data["social_media"].items()
    }
    artist_data.update({"social_media": social_media})
    return artist_data


def _load_artist_data(artist_id: str) -> Dict[str, Any]:
    artist_file_path: Path = STATIC_FOLDER / f"database/artists/{artist_id}.json"
    with open(artist_file_path, mode="r", encoding="utf-8") as artist_file:
        artist_data: Dict[str, Dict[str, Any]] = json.load(artist_file)

    artist_data = _check_personal_and_music_information(artist_data)
    artist_data = _check_social_media(artist_data)

    return artist_data


@APP.route("/")
def home():
    """
    Home page of the Oversized music artist page.

    Returns:
        str: The rendered HTML template for the home page.
    """

    return render_template("home.html")


@APP.route("/artist/<artist_id>")
def artist(artist_id: str):
    """
    Artist page of the Oversized music artist page. Retrieves the artist’s information from a JSON file with the
    specified artist ID and displays it on the page.

    Parameters:
        artist_id (str): The ID of the artist to retrieve information for.

    Returns:
        str: The rendered HTML template for the artist page.
    """

    artist_data: Dict[str, Any] = _load_artist_data(artist_id)
    return render_template("artist.html", artist=artist_data)


def _main() -> None:
    APP.run(debug=True)


if __name__ == "__main__":
    _main()
