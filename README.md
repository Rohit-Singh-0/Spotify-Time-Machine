# Spotify-Time-Machine

---

## Overview

Spotify Time Machine is a Python script that creates a Spotify playlist based on the Billboard Hot 100 songs from a specified date. The script scrapes the Billboard website for the Hot 100 songs on the given date, searches for these songs on Spotify, and creates a private playlist with the retrieved tracks.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- Spotipy library (`pip install spotipy`)

You'll also need to create a Spotify Developer account and obtain your `client_id` and `client_secret` to use the Spotify API.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Rohit-Singh-0/Spotify-Time-Machine.git
    ``

2. Navigate to the project directory:

    ```bash
    cd Spotify-Time-Machine
    ```


4. Open the script (`main.py`) in a text editor and fill in your Spotify Developer credentials (`client_id`, `client_secret`, and `username`).

5. Run the script:

    ```bash
    python main.py
    ```

6. Follow the authentication prompts to authorize the script to access your Spotify account.

7. Enter the date in the YYYY-MM-DD format when prompted.

8. The script will create a private Spotify playlist named "{date} Billboard 100" and add the corresponding songs to it.

## Configuration

- **Client ID and Client Secret**: Obtain these from your Spotify Developer account and replace the placeholders in the script.

- **Redirect URI**: Set up a Redirect URI in your Spotify Developer account and update it in the script.

## Important Note

- The script may not find some songs on Spotify, and these will be skipped during playlist creation.

## Acknowledgments

- This project uses the [Spotipy](https://spotipy.readthedocs.io/) library to interact with the Spotify API.


