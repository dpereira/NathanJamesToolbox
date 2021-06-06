import unittest

from NathanJamesToolbox import Airtable, airtableToolbox


class TestAirtable(unittest.TestCase):

    def test_legacy_interface(self):
        self.assertIs(airtableToolbox, Airtable)

    def test_delete_ids_should_not_call_airtable_when_dry_run_enabled(self):
        at = Airtable("test_base", "test_key", dry_run=True)
        at.delete_ids("test_table", [0, 1, 2, 3, 4])
