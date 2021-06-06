import unittest

from NathanJamesToolbox import Airtable, airtableToolbox


class TestAirtable(unittest.TestCase):

    def test_legacy_interface(self):
        self.assertIs(airtableToolbox, Airtable)
