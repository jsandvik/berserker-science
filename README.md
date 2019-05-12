# berserker-science

This is the backend for a soul calibur 6 frame data app. This serves as the source of truth for all frame data used in the frontend react app [located here](https://github.com/jsandvik/soulcalibur), stored in a mongodb database and served with a flask app api.

## Installation

Install python3 and virtualenv to create your virtual environment for python. Then run `pip install -r requirements.txt` in the home directory. Install mongodb and set your environment variable for `MONGODB_URI` to be the uri for the mongodb instance you are using.

Run `python initialize_db.py` to initialize the database with the current set of frame data.

In order to run the app, the easiest way is to install the heroku dev tools and then run `heroku local`. You can also run `gunicorn sc_guide.api:app`

## How it works
Basically the frame_data directory contains a text file for each character in the game. These originally came out of SCUFFLE output, running through every move for each character. Afterwards, that output's move notation was cleaned up and various other things were added (categorization, break attacks/lethal hits, consolidated mult-hit moves, etc). Whenever a change is made to these files, on deployment running `python initialize_db.py` drops the entire current database and starts importing the current set of frame data in the directory. `scuffle_parser.py` goes through and converts each line into meaningful values to be stored in the mongodb database.

There then exists a simple api that can be queried for that data, that's all in `api.py`. Ultimately this is currently hosted in a free heroku instance at https://berserkerscience.herokuapp.com.
