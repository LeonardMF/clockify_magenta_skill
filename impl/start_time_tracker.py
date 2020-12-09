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

from db import get_user, update_user, create_user

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
    
    msg = _('ASK_PROJECT')
    response = ask(msg)
    return response
