#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell
from skill_sdk.l10n import _


@skill.intent_handler('TEAM_06_START_TIME_TRACKING')
def handler() -> Response:
    """ Handler of TEAM_06_START_TIME_TRACKING intent,
        TEAM_06_START_TIME_TRACKING intent is activated when user says 'zeiterfassung starten'
        returns question for project

    :return:        Response
    """
    # We get a translated message
    msg = _('ASK_PROJECT')
    # We create a simple response
    response = tell(msg)
    # We return the response
    return response
