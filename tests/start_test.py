#
# voice-skill-sdk
#
# (C) 2020, YOUR_NAME (YOUR COMPANY), Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
import unittest

from impl.start_time_tracker import skill


class TestMain(unittest.TestCase):

    # def test_open_handler(self):
        
    #     response = skill.test_intent('TEAM_06_OPEN_TIME_TRACKING')
    #     self.assertEqual(response.text.key, 'WELCOME_NEW_USER WELCOME_SELECTION')

    def test_start_handler(self):
        
        response = skill.test_intent('TEAM_06_START_TIME_TRACKING')
        self.assertEqual(response.text.key, 'ASK_PROJECT')
    
    # def test_add_project_handler(self):
        
    #     response = skill.test_intent('TEAM_06_ADD_PROJECT', project="Test Projekt")
    #     self.assertEqual(response.text.key, 'ASK_TASK')

    # def test_add_task_handler(self):
        
    #     response = skill.test_intent('TEAM_06_ADD_TASK', task="Test Aufgabe")
    #     self.assertEqual(response.text.key, 'START_COMFIRMATION')

    

    

