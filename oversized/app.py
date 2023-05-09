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

from datetime import datetime
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


def _read_artist_data(artist_id: str) -> Dict[str, Any]:
    artist_file_path: Path = STATIC_FOLDER / f"database/artists/{artist_id}.json"
    with open(artist_file_path, mode="r", encoding="utf-8") as artist_file:
        artist_data: Dict[str, Any] = json.load(artist_file)
    return artist_data


def _add_artist_image(artist_data: Dict[str, Any], artist_id: str) -> None:
    artist_image: str = f"images/artists/{artist_id}.jpg"
    if (STATIC_FOLDER / artist_image).exists():
        artist_data["image"] = artist_image


def _format_genres(artist_data: Dict[str, Any]) -> None:
    if "genres" in artist_data:
        artist_data["genres"] = ", ".join(artist_data["genres"])


def _format_other_names(artist_data: Dict[str, Any]) -> None:
    if "personal_information" in artist_data and "other_names" in artist_data["personal_information"]:
        artist_data["personal_information"]["other_names"] = ", ".join(
            artist_data["personal_information"]["other_names"]
        )


def _format_birthdate(artist_data: Dict[str, Any]) -> None:
    if "personal_information" in artist_data and "birthdate" in artist_data["personal_information"]:
        artist_data["personal_information"]["birthdate"] = datetime.strptime(
            artist_data["personal_information"]["birthdate"], "%Y-%m-%d"
        ).strftime("%B %d, %Y")


def _format_social_medias(artist_data: Dict[str, Any]) -> None:
    if "social_medias" in artist_data:
        social_medias: Dict[str, Dict[str, str]] = {}
        for platform_id, user in artist_data["social_medias"].items():
            platform_name, url = SOCIAL_MEDIAS[platform_id]
            social_medias[platform_id] = {"platform_name": platform_name, "url": url.replace("<user>", user)}
        artist_data["social_medias"] = social_medias


def _load_artist_data(artist_id: str) -> Dict[str, Any]:
    artist_data: Dict[str, Any] = _read_artist_data(artist_id)

    _add_artist_image(artist_data, artist_id)

    _format_genres(artist_data)
    _format_other_names(artist_data)
    _format_birthdate(artist_data)
    _format_social_medias(artist_data)

    return artist_data


@APP.route("/")
def home() -> str:
    """
    Home page of the Oversized music artist page.

    Returns:
        str: The rendered HTML template for the home page.
    """

    return render_template("home.html")


@APP.route("/artist/<artist_id>")
def artist(artist_id: str) -> str:
    """
    Artist page of the Oversized music artist page. Retrieves the artist’s information from a JSON file with the
    specified artist ID and displays it on the page.

    Parameters:
        artist_id (str): The ID of the artist to retrieve information for.

    Returns:
        str: The rendered HTML template for the artist page.
    """

    return render_template("artist.html", artist=_load_artist_data(artist_id))


def _main() -> None:
    APP.run(debug=True)


if __name__ == "__main__":
    _main()
