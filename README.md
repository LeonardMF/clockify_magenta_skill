# Time Tracker

With Time Tracker skill you can track your working hours in [Clockify](https://clockify.me) via Voice using the Magenta Speaker.
It uses the [SDK for Python](https://github.com/telekom/voice-skill-sdk). Initial development during the [Remote Rhapsody Online Hackathon](https://remote-rhapsody-platform.hubraum.com/).
There is an additional [registration service](https://github.com/LeonardMF/clockify_registration-service) with own website to onboard new Users.

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

## Video

Watch the demos of the prototype in my [Project Presentation](https://docs.google.com/presentation/d/1qD0rEdwrFhqxXym_j6HMXmzUHc4KGJ796hc7DXoMVxc/edit?usp=sharing). Here are the download links of the videos:

- [01_Start.mp4](https://drive.google.com/file/d/1NrN9gIJpwgFesvRjX0s_bPdLR5DaIT0Z/view?usp=sharing)
- [12_Stop.mp4](https://drive.google.com/file/d/1OlkpMHC_o0PjVgCSGP8sp8T4p9yVlExU/view?usp=sharing)
- [23_Show.mp4](https://drive.google.com/file/d/1A6awKQ-5tJH3BR19r9Pn88Rjl77upNDI/view?usp=sharing)
- [31_New_User.mp4](https://drive.google.com/file/d/15Br4qbf9lQ1_eNy3nJ3Mp-syecRsE8db/view?usp=sharing)
- [32_App.mp4](https://drive.google.com/file/d/18Xm5opPfhkMtblQJlLNaFrDZ6ra__KL0/view?usp=sharing)
- [33_Onboarded_User.mp4](https://drive.google.com/file/d/1AGx0X6WgfnRlebatjLRlEAV5DUCVGxyz/view?usp=sharing)
- [41_Show.mp4](https://drive.google.com/file/d/1cgaBL-xNGKRbvHtYsMZ9QouP7NgksQRZ/view?usp=sharing)
- [42_Card.mp4](https://drive.google.com/file/d/1oCSb7cTTAoQD34wE-sk6P9CLtUQC0-XS/view?usp=sharing)

## Deployment 
