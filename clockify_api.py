import json
import requests
import pytz
from datetime import datetime
from decouple import config

API_BASE_URL = "https://api.clockify.me/api/v1"
CLOCKIFY_API_KEY = config('CLOCKIFY_API_KEY')

header = {'X-Api-Key': CLOCKIFY_API_KEY,
          'content-type':'application/json'}


def get_clockify():
    url = API_BASE_URL + "/user"

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info["id"]
        email = user_info["email"]
        active_workspace_id = user_info["activeWorkspace"]
        default_workspace_id = user_info["defaultWorkspace"]
        timeZone = user_info["settings"]["timeZone"]

        return {'user_id': user_id, 'active_workspace_id': active_workspace_id} 
    else:
        print("User not found!")
        return None

def get_projects(workspace_id):
    url = API_BASE_URL + "/workspaces/{workspaceId}/projects".format(workspaceId=workspace_id)

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        projects_dict = {}
        projects = response.json()

        for project in projects:
            id = project["id"]
            name = project["name"]
            projects_dict[name] = id

        return projects_dict
    else:
        print("Projects not found!")
        return None

def get_project_ids(workspace_id):
    url = API_BASE_URL + "/workspaces/{workspaceId}/projects".format(workspaceId=workspace_id)

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        projects_dict = {}
        projects = response.json()

        for project in projects:
            id = project["id"]
            name = project["name"]
            projects_dict[id] = name

        return projects_dict
    else:
        print("Projects not found!")
        return None

def add_project(workspace_id, project_name):
    url = API_BASE_URL + "/workspaces/{workspaceId}/projects".format(workspaceId=workspace_id)
    data = {"name": project_name,
            "clientId": "",
            "isPublic": "false",
            "estimate": {
                "estimate": 3600,
                "type": "AUTO"
            },
            "color": "#ea0a8e",
            "note": "This is project's note",
            "billable": "true"}
    data_json = json.dumps(data)
    response = requests.post(url, headers=header, data=data_json)
    
    if response.status_code == 201:
        
        project = response.json()
        id = project["id"]
        name = project["name"]
        return {name: id}
    else:
        print("Project could not be added!")
        return None

def get_time_entries(workspace_id, user_id):
    url = API_BASE_URL + "/workspaces/{workspaceId}/user/{userId}/time-entries".format(workspaceId=workspace_id,userId=user_id)
    
    response = requests.get(url, headers=header)
    
    if response.status_code == 200:
        time_entries = response.json()

        return time_entries
    else:
        print("Time entries not found!")
        return None

def add_time_entrie(workspace_id, project_id, task_description, start_datetime, end_datetime=None):
    url = API_BASE_URL + "/workspaces/{workspaceId}/time-entries".format(workspaceId=workspace_id)
    data = {"start": start_datetime,
            "billable": "true",
            "description": task_description,
            "projectId": project_id,
            "end": end_datetime}

    data_json = json.dumps(data)
    response = requests.post(url, headers=header, data=data_json)
    
    if response.status_code == 201:
        
        time_entrie = response.json()
        
        return time_entrie
    else:
        print("Time entrie could not be added!")
        return None

def get_time_entrie(workspace_id, time_entry_id):
    url = API_BASE_URL + "/workspaces/{workspaceId}/time-entries/{timeEntryId}".format(workspaceId=workspace_id,timeEntryId=time_entry_id)

    response = requests.get(url, headers=header)
    
    if response.status_code == 200:
        
        time_entrie = response.json()
        
        return time_entrie
    else:
        print("Time entrie could not be stoped!")
        return None

# To stop the timer, you'll have to use the "PUT /workspaces/{workspaceId}/time-entries/{timeEntryId}/end" PATH (request example: {"end":"2019-02-07T14:00:07.000Z"}
# Does not work!
# Works with "PUT /workspaces/{workspaceId}/time-entries/{timeEntryId}" with  {"start": "2020-11-28T11:00:00Z","end":"2019-02-07T14:00:07.000Z"}
def end_time_entrie(workspace_id, time_entrie_id, start_datetime, end_datetime):

    url = API_BASE_URL + "/workspaces/{workspaceId}/time-entries/{timeEntryId}".format(workspaceId=workspace_id,timeEntryId=time_entrie_id)

    data = {"start": start_datetime,
            "end": end_datetime}

    data_json = json.dumps(data)
    response = requests.put(url, headers=header, data=data_json)
    
    if response.status_code == 200:
        
        time_entrie = response.json()
        
        return time_entrie
    else:
        print("Time entrie could not be stoped!")
        return None


def stop_time_entrie(workspace_id, user_id, end_datetime):
    url = API_BASE_URL + "/workspaces/{workspaceId}/user/{userId}/time-entries".format(workspaceId=workspace_id,userId=user_id)

    data = {"end": end_datetime}

    data_json = json.dumps(data)
    response = requests.patch(url, headers=header, data=data_json)
    
    if response.status_code == 200:
        
        time_entrie = response.json()
        
        return time_entrie
    else:
        print("Time entrie could not be stoped!")
        return None

def check_running_timer(time_entries):
    for time_entrie in time_entries:
        if time_entrie['timeInterval']['end'] == None:
            return time_entrie

    return None


if __name__ == '__main__':
    clockify = get_clockify()
    clockify_id = clockify['user_id']
    workspace_id = clockify['active_workspace_id']
    projects = get_projects(workspace_id)
    project_ids = get_project_ids(workspace_id)

    # print(projects)

    # new_project = add_project(workspace_id,"Pitch")
    # print(new_project)

    time_entries = get_time_entries(workspace_id, clockify_id)
     
    project_id = projects["Alexa Skill"]
    task_description = "implement clockify api"

    now = datetime.utcnow()
    now_str = now.isoformat()
    now_str = now_str.split('.')[0] + ".000Z"

    # start_datetime = "2020-11-28T19:30:00.000Z"
    # end_datetime = "2020-11-28T20:53:00.000Z"
    
    # print(add_time_entrie(workspace_id, project_id, task_description, now_str, end_datetime=None))

    # running_timer = check_running_timer(time_entries)

    # if running_timer:
    #     # time_entrie = end_time_entrie(workspace_id, running_timer["id"], running_timer["timeInterval"]["start"], end_datetime)
        
    #     time_entrie =  stop_time_entrie(workspace_id, user_id=clockify_id, end_datetime=now_str)
    #     print(time_entrie)
    #     project = project_ids[time_entrie['projectId']]
    #     duration = time_entrie['timeInterval']['duration']
    #     task = time_entrie['description']
    #     print(project)
    #     print(duration)
    #     print(task)

    entries = get_time_entries(workspace_id, clockify_id)

    time_entrie = entries[0]

    project = project_ids[time_entrie['projectId']]


    duration = time_entrie['timeInterval']['duration']
    task = time_entrie['description']
    print(project)
    print(duration)
    print(task)