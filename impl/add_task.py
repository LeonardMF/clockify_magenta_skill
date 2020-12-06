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

    if project == '':
        msg = _('ASK_PROJECT')
        response = ask(msg)
    elif task == '':
        msg = _('ASK_TASK')
        response = ask(msg)
    else:
        # ToDo: Start time tracking
        msg = _('START_COMFIRMATION')
        response = tell(msg)

    return response
