import unittest

import src.versioncommand as versioncommand

class TestVersionCommand(unittest.TestCase):
    def setUp(self):
        self.command = versioncommand.VersionCommand()

    def test_begin_returns_none(self):
        result = self.command.begin()
        self.assertEqual(result, None)

    def test_process_raises_exception(self):
        self.command.begin()
        with self.assertRaises(Exception):
            self.command.process('Ignored input')

    def test_end_returns_version_string(self):
        self.command.begin()
        result = self.command.end()
        self.assertEquals(result, 'Version 0.1')
