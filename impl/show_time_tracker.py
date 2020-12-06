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


@skill.intent_handler('TEAM_06_SHOW_TIME_TRACKING')
def handler() -> Response:
    """ Handler of TEAM_06_SHOW_TIME_TRACKING intent,
        TEAM_06_SHOW_TIME_TRACKING intent is activated when user says 'Stunden'
        returns booked working hours

    :return:        Response
    """

    msg = "Bislang wurden keine Stunden erfasst."

    response = tell(msg)
    return response
