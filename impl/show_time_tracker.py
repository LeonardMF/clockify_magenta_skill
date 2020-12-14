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

from clockify_api import check_running_timer, get_clockify, get_project_ids, get_projects, get_time_entries
from helper import parse_duration, get_random_string
from db import create_user, get_clockify_api_key, get_user, get_user_token, set_user_token, update_user

def get_auth_url(token) -> str:

    return "http://clockify-auth-client.s3-website.eu-central-1.amazonaws.com/" + "?user_token={token}".format(token=token)

def get_clockify_url() -> str:

    return "https://www.clockify.me/tracker"

@skill.intent_handler('TEAM_06_SHOW_TIME_TRACKING')
def handler(user_id: str) -> Response:
    """ Handler of TEAM_06_SHOW_TIME_TRACKING intent,
        TEAM_06_SHOW_TIME_TRACKING intent is activated when user says 'Stunden'
        returns booked working hours

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

        try:
            clockify = get_clockify(clockify_api_key)
            clockify_id = clockify['user_id']
            workspace_id = clockify['active_workspace_id']
            project_ids = get_project_ids(clockify_api_key, workspace_id)
            time_entries = get_time_entries(clockify_api_key, workspace_id, clockify_id)

            time_entrie = time_entries[0]
            if time_entrie['timeInterval']['duration'] is None:
                time_entrie = time_entries[1]

            if time_entrie:
                project = project_ids[time_entrie['projectId']]
                duration = parse_duration(time_entrie['timeInterval']['duration'])
                task = time_entrie['description']
                msg = _("SHOW_TIME", project=project, duration=duration, task=task)
                response = tell(msg)
                response.card = Card(
                    type_="GENERIC_DEFAULT",
                    title="Time Tracker: Clockify Link",
                    text="Hier ist der Link zu deinen gebuchten Stunden:",
                    action=get_clockify_url(),
                    action_text="Öffnen"
                )
            else: 
                msg = _("SHOW_ERROR")
                response = tell(msg)
        except:
            msg = _("SHOW_ERROR")
            response = tell(msg)
    return response
