# Time Tracker

With Time Tracker skill you can track your working hours in Clockify via Voice.

## Active virtual enviroment

    $ source .venv/bin/activate 
    
## Test

    $ python manage.py test 

**BUG:** `sssssssA translation for locale de is not available.`
*Note:* Try translation with `msgfmt de.po -o de.mo`

## Run 

    $ python manage.py --dev run

The Skill runs at http://localhost:4242/.

Expose the locally running skill via ngrok: 

    $ ./ngrok http 4242 --subdomain time-tracker

