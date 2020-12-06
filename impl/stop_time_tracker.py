#
# voice-skill-sdk
#
# (C) 2020, Leonard Fuechsel
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell
from skill_sdk.l10n import _


@skill.intent_handler('TEAM_06_STOP_TIME_TRACKING')
def handler() -> Response:
    """ Handler of TEAM_06_STOP_TIME_TRACKING intent,
        TEAM_06_STOP_TIME_TRACKING intent is activated when user says 'zeiterfassung stoppen'
        stops running timer 

    :return:        Response
    """
    # ToDo: Get time tracking status
    time_tracking_on = True

    if time_tracking_on:
        # ToDo: Stop time tracking
        msg = _('STOP_COMFIRMATION')
    else:
        msg = _('STOP_ERROR')
    
    response = tell(msg)
    return response
