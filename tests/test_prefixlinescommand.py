import unittest

import src.prefixlinescommand as prefixlinescommand

class TestPrefixLinesCommand(unittest.TestCase):
    def setUp(self):
        self.command = prefixlinescommand.PrefixLinesCommand()

    def test_expects_input_returns_true(self):
        result = self.command.expects_input
        self.assertEqual(result, True)

    def test_prefix_can_be_set(self):
        self.command.prefix = 'test'
        self.assertEqual(self.command.prefix, 'test')

    def test_begin_returns_none(self):
        result = self.command.begin()
        self.assertEqual(result, None)

    def test_process_returns_input_when_prefix_is_empty_string(self):
        self.command.prefix = ''
        self.command.begin()
        input = 'Line 1'
        result = self.command.process(input)
        self.assertEqual(result, input)

    def test_process_prefixes_line(self):
        self.command.prefix = '001'
        self.command.begin()
        result = self.command.process('Line')
        self.assertEqual(result, '001Line')

    def test_end_returns_none(self):
        self.command.begin()
        result = self.command.end()
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()

