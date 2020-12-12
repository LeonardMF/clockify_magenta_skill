# Time Tracker

With Time Tracker skill you can track your working hours in [Clockify](https://clockify.me) via Voice using the Magenta Speaker.
It uses the [SDK for Python](https://github.com/telekom/voice-skill-sdk). Initial development during the [Remote Rhapsody Online Hackathon](https://remote-rhapsody-platform.hubraum.com/).

## Prerequisites

Python: 3.8.4

## Create Virtual Environment
Follow the instruction in der [Docs](https://docs.python.org/3/tutorial/venv.html):

    $ python -m venv venv

Active virtual enviroment:

    $ source venv/bin/activate

Freeze the requirements:
    $ pip freeze > requirements.txt

## Install 

    $ pip install -r requirements.txt

Freeze the new requirements:

    $ pip freeze > requirements.txt

## Environment Variables

This project uses environment variables are stored in `.env`, using [Python Decouple](https://pypi.org/project/python-decouple/).   
    
## Test

Execute Unittests: 

    $ python manage.py test 

**BUG:** `sssssssA translation for locale de is not available.` <br>
*Note:* Try translation with `msgfmt de.po -o de.mo`

## Run 

To run the skill locally:

    $ python manage.py --dev run

The Skill runs at http://localhost:4242/. You can check the [Swagger](http://localhost:4242/) API there.

Expose the locally running skill via ngrok: 

    $ ./ngrok http 4242 --subdomain time-tracker

## Deployment 
