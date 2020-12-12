#
# voice-skill-sdk
#
# (C) 2020, Leonard Fuechsel
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import Response, ask, skill, ssml, tell, Card
from skill_sdk.l10n import _

from clockify_api import check_running_timer, get_clockify, get_time_entries
from db import create_user, get_clockify_api_key, get_user, get_user_token, set_user_token, update_user
from helper import get_random_string

def get_auth_url(token) -> str:

    return "http://clockify-auth-client.s3-website.eu-central-1.amazonaws.com/" + "?user_token={token}".format(token=token)

@skill.intent_handler('TEAM_06_OPEN_TIME_TRACKING')
def handler(user_id: str) -> Response:
    """ Handler of TEAM_06_OPEN_TIME_TRACKING intent,
        TEAM_06_OPEN_TIME_TRACKING intent is activated when user says 'zeiterfassung stoppen'
        welcomes user

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
        clockify = get_clockify(clockify_api_key)
        clockify_id = clockify['user_id']
        workspace_id = clockify['active_workspace_id']
        time_entries = get_time_entries(clockify_api_key=clockify_api_key, workspace_id=workspace_id, user_id=clockify_id)
        running_timer = check_running_timer(time_entries)
        # Get time tracking status
        if running_timer:
            msg = _('WELCOME_RETURNING_USER')
            msg = msg + " " + _('WELCOME_STOP_SELECTION')
        else:
            msg = _('WELCOME_SELECTION')
            
        response = ask(msg)

    return response
