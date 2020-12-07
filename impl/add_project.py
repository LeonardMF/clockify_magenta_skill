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

# from clockify_api import get_clockify, get_projects

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

    # # ToDo: Check project_id
    # clockify = get_clockify()
    # clockify_id = clockify['user_id']
    # workspace_id = clockify['active_workspace_id']
    # projects = get_projects(workspace_id)
    # project_id = projects[project]

    msg = _('ASK_TASK')
    response = ask(msg)
    return response
