import boto3
import pytz

from decouple import config
from datetime import datetime
from decimal import Decimal

LMF_AWS_ACCESS_KEY_ID = config('LMF_AWS_ACCESS_KEY_ID')
LMF_AWS_SECRET_ACCESS_KEY = config('LMF_AWS_SECRET_ACCESS_KEY')

LMF_AWS_DB_REGION = config('LMF_AWS_DB_REGION')
LMF_AWS_TABLE_NAME = config('LMF_AWS_TABLE_NAME')
TIME_ZONE = config('TIME_ZONE')

dynamodb = boto3.resource('dynamodb', region_name=LMF_AWS_DB_REGION, aws_access_key_id=LMF_AWS_ACCESS_KEY_ID, aws_secret_access_key=LMF_AWS_SECRET_ACCESS_KEY)
table = dynamodb.Table(LMF_AWS_TABLE_NAME)

def create_user(user_id):

    tz = pytz.timezone(TIME_ZONE)
    now = datetime.now(tz)
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")

    try:
        response = table.put_item(
                    Item = { "user_id": user_id,
                             "created_at": now_str,
                             "last_used_at": now_str,
                             "sessions_count": 1 })
    except:
        print("User could not be created")
        return None
    else:
        return response

def get_user(user_id):

    try:
        response = table.get_item(
                Key = { 'user_id': user_id })

        item = response['Item']
    except:
        print("User not found!")
        return None
    else:
        return item

def update_user(user_info):

    try:
        tz = pytz.timezone(TIME_ZONE)
        now = datetime.now(tz)
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")
        sessions_count = user_info["sessions_count"] + 1

        response = table.update_item(
                Key = {
                        'user_id': user_info["user_id"]
                },
                UpdateExpression="set sessions_count=:s_c, last_used_at=:l_u_a",
                ExpressionAttributeValues={
                    ':s_c': Decimal(sessions_count),
                    ':l_u_a': now_str,
                },
        )
    except:
        print("User not updated!")
        return False
    else:
        return True

def set_project(user_id, project_name):

    try:
        response = table.update_item(
                Key = {
                        'user_id': user_id
                },
                UpdateExpression="set project_name=:p_n",
                ExpressionAttributeValues={
                    ':p_n': project_name,
                },
        )
    except:
        print("Project could not be added!")
        return False
    else:
        return True

def get_project(user_id):

    try:
        response = table.get_item(
                Key = { 'user_id': user_id })

        project = response['Item']['project_name']
    except:
        print("Project not found!")
        return None
    else:
        return project

def set_task(user_id, task):

    try:
        response = table.update_item(
                Key = {
                        'user_id': user_id
                },
                UpdateExpression="set task=:t",
                ExpressionAttributeValues={
                    ':t': task,
                },
        )
    except:
        print("Task could not be added!")
        return False
    else:
        return True

def get_task(user_id):

    try:
        response = table.get_item(
                Key = { 'user_id': user_id })

        task = response['Item']['task']
    except:
        print("Task not found!")
        return None
    else:
        return task


if __name__ == '__main__':

    user_id = "TestId"
    user_info = get_user(user_id)
   
    if user_info:
        update_user(user_info)
    else: 
        create_user(user_id)

    # print(get_user(user_id))

    # project_name="Alexa Skill"

    # set_project(user_id,project_name)
    
    task = "Datenbank anbinden"

    # set_task(user_id, task)

    print(get_project(user_id))

    print(get_task(user_id))

