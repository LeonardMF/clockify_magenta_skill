#
# voice-skill-sdk
#
# (C) 2020, Leonard Fuechsel
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, ask
from skill_sdk.l10n import _


@skill.intent_handler('TEAM_06_ADD_PROJECT')
def handler(project: str) -> Response:
    """ Handler of TEAM_06_ADD_PROJECT intent,
        TEAM_06_ADD_PROJECT intent is activated when user says '[Aa]m (?P<project>.*)'
        returns question for task

    :return:        Response
    """

    project = project
    print('Project: ', project)
    # ToDo: Set project in context
    msg = _('ASK_TASK')
    response = ask(msg)
    return response
