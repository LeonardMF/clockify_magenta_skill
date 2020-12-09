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
from skill_sdk import skill, Response, tell
from skill_sdk.l10n import _

from clockify_api import get_clockify, get_projects, get_time_entries, check_running_timer, stop_time_entrie, get_project_ids
from db import set_project, set_task
from helper import parse_duration


@skill.intent_handler('TEAM_06_STOP_TIME_TRACKING')
def handler(user_id:str) -> Response:
    """ Handler of TEAM_06_STOP_TIME_TRACKING intent,
        TEAM_06_STOP_TIME_TRACKING intent is activated when user says 'zeiterfassung stoppen'
        stops running timer 

    :return:        Response
    """
    clockify = get_clockify()
    clockify_id = clockify['user_id']
    workspace_id = clockify['active_workspace_id']
    time_entries = get_time_entries(workspace_id, clockify_id)
    project_ids = get_project_ids(workspace_id)

    # Get time tracking status
    running_timer = check_running_timer(time_entries)

    if running_timer:
        # Stop time tracking
        now = datetime.utcnow()
        now_str = now.isoformat()
        now_str = now_str.split('.')[0] + ".000Z"
        time_entrie = stop_time_entrie(workspace_id, user_id=clockify_id, end_datetime=now_str)

        project = project_ids[time_entrie['projectId']]
        duration = parse_duration(time_entrie['timeInterval']['duration'])
        task = time_entrie['description']

        set_project(user_id,'')
        set_task(user_id,'')

        msg = _('STOP_COMFIRMATION',project=project, task=task, duration=duration)
    else:
        msg = _('STOP_ERROR')
    
    response = tell(msg)
    return response
