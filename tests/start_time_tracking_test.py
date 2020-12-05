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

    def test_hello_handler(self):
        
        response = skill.test_intent('TEAM_06_START_TIME_TRACKING')
        self.assertEqual(response.text.key, 'ASK_PROJECT')
