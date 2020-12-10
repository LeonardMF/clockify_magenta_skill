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

from clockify_api import get_clockify, get_projects, get_project_ids, get_time_entries
from helper import parse_duration

@skill.intent_handler('TEAM_06_SHOW_TIME_TRACKING')
def handler() -> Response:
    """ Handler of TEAM_06_SHOW_TIME_TRACKING intent,
        TEAM_06_SHOW_TIME_TRACKING intent is activated when user says 'Stunden'
        returns booked working hours

    :return:        Response
    """

    clockify = get_clockify()
    clockify_id = clockify['user_id']
    workspace_id = clockify['active_workspace_id']
    project_ids = get_project_ids(workspace_id)
    time_entries = get_time_entries(workspace_id, clockify_id)

    time_entrie = time_entries[0]

    if time_entries[0]:
        project = project_ids[time_entries[0]['projectId']]
        duration = parse_duration(time_entries[0]['timeInterval']['duration'])
        task = time_entries[0]['description']
        msg = _("SHOW_TIME", project=project, duration=duration, task=task)
    else: 
        msg = _("SHOW_ERROR")

    response = tell(msg)
    return response
