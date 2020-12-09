#
# voice-skill-sdk
#
# (C) 2020, Leonard Fuechsel
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell, ask
from skill_sdk.l10n import _

from clockify_api import check_running_timer, get_clockify, get_time_entries

@skill.intent_handler('TEAM_06_OPEN_TIME_TRACKING')
def handler() -> Response:
    """ Handler of TEAM_06_OPEN_TIME_TRACKING intent,
        TEAM_06_OPEN_TIME_TRACKING intent is activated when user says 'zeiterfassung stoppen'
        welcomes user

    :return:        Response
    """

    #ToDo: Get user id
    # user_id = ''
    # returning_user = False
    # if returning_user:
    #     msg = _('WELCOME_RETURNING_USER')
    # else: 
    #     msg = _('WELCOME_NEW_USER')

    clockify = get_clockify()
    clockify_id = clockify['user_id']
    workspace_id = clockify['active_workspace_id']
    time_entries = get_time_entries(workspace_id, clockify_id)

    # Get time tracking status
    running_timer = check_running_timer(time_entries)

    if running_timer:
        msg = _('WELCOME_RETURNING_USER')
        msg = msg + " " + _('WELCOME_STOP_SELECTION')
    else:
        msg = _('WELCOME_NEW_USER')
        msg = msg + " " + _('WELCOME_SELECTION')
        
    response = ask(msg)
    return response
