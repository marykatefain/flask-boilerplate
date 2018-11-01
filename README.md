# Flask BoilerPlate

A basic boilerplate flask app to get you started


## Local Development

1. Clone the repo

2. `pip install -r requirements.txt`

3. Start the server:

`FLASK_APP=server.py SECRET_KEY=you-need-to-generate-me gunicorn server:app --bind 0.0.0.0:5000`

This should start a local server at `http://127.0.0.1:5000/`

## Running Tests

You will need to pass the same config vars into the tests:

`SECRET_KEY=you-need-to-generate-me python tests.py`


## Deploying

`git push dokku master`
