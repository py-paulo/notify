from unittest import TestCase
from notify.notify import Notify


class TestNotify(TestCase):
    def test_class_notify(self):
        nf = Notify(enable_teams=True, enable_slack=True, enable_errors=False)
        self.assertEqual(nf.enable_teams, False)
        self.assertEqual(nf.enable_slack, False)
        nf = Notify(
            enable_teams=True, enable_slack=True, enable_errors=False, teams_webhook_url='https://url...')
        self.assertEqual(nf.enable_teams, True)
        self.assertEqual(nf.enable_slack, False)
