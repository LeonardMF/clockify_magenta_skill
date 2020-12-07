#
# voice-skill-sdk
#
# (C) 2020, Leonard Fuechsel
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from datetime import datetime

from skill_sdk import skill, Response, tell, ask
from skill_sdk.l10n import _

from clockify_api import get_clockify, get_projects, add_time_entrie

#@skill.intent_handler('TEAM_06_START_TIME_TRACKING')
@skill.intent_handler('TEAM_06_ADD_TASK')
def handler(task: str) -> Response:
    """ Handler of TEAM_06_ADD_TASK intent,
        TEAM_06_ADD_TASK intent is activated when user says '(ich möchte|ich werde) (die|den|das)(?P<task>.*)'
        returns confirmation start timer

    :return:        Response
    """
    task = task
    print('Task: ', task)
    task = "Intents implementieren"
    # ToDo: Get project from context
    project = 'Magenta Skill'
    

    clockify = get_clockify()
    clockify_id = clockify['user_id']
    workspace_id = clockify['active_workspace_id']
    projects = get_projects(workspace_id)
    project_id = projects[project]

    if project == '':
        msg = _('ASK_PROJECT')
        response = ask(msg)
    elif task == '':
        msg = _('ASK_TASK')
        response = ask(msg)
    else:
        # Start time tracking
        now = datetime.utcnow()
        now_str = now.isoformat()
        now_str = now_str.split('.')[0] + ".000Z"

        add_time_entrie(workspace_id, project_id, task, now_str, end_datetime=None)

        msg = _('START_COMFIRMATION')
        response = tell(msg)

    return response
