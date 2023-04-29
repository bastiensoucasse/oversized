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

from flask import Flask, json, render_template

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """
    Retrieves artist information from a JSON file and renders it in an HTML template.

    Returns:
    A rendered HTML template that displays the artist’s information.

    Raises:
    FileNotFoundError: If the artist.json file cannot be found in the "static" directory.
    """

    with open("oversized/artist.json", "r", encoding="utf-8") as artist_file:
        artist = json.load(artist_file)

    return render_template("artist.html", artist=artist)


def _main() -> None:
    app.run(debug=True)


if __name__ == "__main__":
    _main()
