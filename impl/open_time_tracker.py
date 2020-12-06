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


@skill.intent_handler('TEAM_06_OPEN_TIME_TRACKING')
def handler() -> Response:
    """ Handler of TEAM_06_OPEN_TIME_TRACKING intent,
        TEAM_06_OPEN_TIME_TRACKING intent is activated when user says 'zeiterfassung stoppen'
        welcomes user

    :return:        Response
    """

    #ToDo: Get user id
    user_id = ''
    returning_user = False

    if returning_user:
        msg = _('WELCOME_RETURNING_USER')
    else: 
        msg = _('WELCOME_NEW_USER')

    # ToDo: Get time tracking status
    time_tracking_on = False

    if time_tracking_on:
        msg = msg + " " + _('WELCOME_STOP_SELECTION')
    else:
        msg = msg + " " + _('WELCOME_SELECTION')
        
    response = ask(msg)
    return response
