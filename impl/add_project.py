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
from db import set_project

@skill.intent_handler('TEAM_06_ADD_PROJECT')
def handler(user_id: str, project: str) -> Response:
    """ Handler of TEAM_06_ADD_PROJECT intent,
        TEAM_06_ADD_PROJECT intent is activated when user says '[Aa]m (?P<project>.*)'
        returns question for task

    :return:        Response
    """
    
    # # ToDo: Check project_id
    # clockify = get_clockify()
    # clockify_id = clockify['user_id']
    # workspace_id = clockify['active_workspace_id']
    # projects = get_projects(workspace_id)
    # project_id = projects[project]

    if set_project(user_id, project):
        msg = _('ASK_TASK')
    else:
        msg = _('ASK_PORJECT')
    response = ask(msg)
    return response
