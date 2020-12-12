#
# voice-skill-sdk
#
# (C) 2020, Leonard Fuechsel
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell, ask, Card
from skill_sdk.l10n import _

from db import create_user, get_clockify_api_key, get_user, get_user_token, set_user_token, update_user
from helper import get_random_string

def get_auth_url(token) -> str:

    return "http://clockify-auth-client.s3-website.eu-central-1.amazonaws.com/" + "?user_token={token}".format(token=token)

@skill.intent_handler('TEAM_06_START_TIME_TRACKING')
def handler(user_id: str) -> Response:
    """ Handler of TEAM_06_START_TIME_TRACKING intent,
        TEAM_06_START_TIME_TRACKING intent is activated when user says 'zeiterfassung starten'
        returns question for project

    :return:        Response
    """

    user_info = get_user(user_id)
   
    if user_info:
        update_user(user_info)
    else: 
        create_user(user_id)

    clockify_api_key = get_clockify_api_key(user_id)

    if clockify_api_key is None or clockify_api_key == '':
        user_token = get_user_token(user_id)
        
        if user_token is None or user_token == '':
            user_token = get_random_string(4)
            set_user_token(user_id, user_token)

        msg = _('WELCOME_NEW_USER')

        response = tell(msg)

        response.card = Card(
            type_="GENERIC_DEFAULT",
            title="Time Tracker: Hinterlege deinen Clockify Account",
            text="User Token: {token}".format(token=user_token),
            action=get_auth_url(token=user_token),
            action_text="Klick hier, um einen Account zu hinterlegen."
        )
    else:
        msg = _('ASK_PROJECT')
        response = ask(msg)
        
    return response
