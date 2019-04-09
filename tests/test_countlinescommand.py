import unittest

import src.countlinescommand as countlinescommand

class TestCountLinesCommand(unittest.TestCase):
    def setUp(self):
        self.command = countlinescommand.CountLinesCommand()

    def test_expects_input_returns_true(self):
        result = self.command.expects_input
        self.assertEqual(result, True)

    def test_begin_returns_none(self):
        result = self.command.begin()
        self.assertEqual(result, None)

    def test_process_returns_input(self):
        self.command.begin()
        input = 'Line 1'
        result = self.command.process(input)
        self.assertEqual(result, input)

    def test_end_returns_zero_when_no_lines(self):
        self._test_lines(0)

    def test_end_returns_1_when_1_line(self):
        self._test_lines(1)

    def test_end_returns_10_when_10_line(self):
        self._test_lines(10)

    def _test_lines(self, count):
        self.command.begin()
        for line_index in range(0, count):
            self.command.process('Line %s'.format(line_index))
        result = str(self.command.end())
        self.assertEqual(result, str(count))



if __name__ == '__main__':
    unittest.main()

