import unittest

import src.countlinescommand as countlinescommand

class TestCountLinesCommand(unittest.TestCase):
    def test_execute(self):
        command = countlinescommand.CountLinesCommand()
        command.execute()
        pass

if __name__ == '__main__':
    unittest.main()

