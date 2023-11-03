import os
import re

import commandlineargumentexception
import commandparser

class FormatTimesheetCommandParser(commandparser.CommandParser):
    def fill_command(self, args):
        return FormatTimesheetCommand()

class FormatTimesheetCommand(commandparser.BufferedCommand):
    def __init__(self):
        super().__init__()
        entryLinePattern = '^(?P<start>\\d{2}:\\d{2})\\s+'
        entryLinePattern += '((?P<end>\\d{2}:\\d{2})\\s+)?'
        entryLinePattern += '\\[(?P<code>\\S+)\\s+'
        entryLinePattern += '(?P<task>[^,]+)'
        entryLinePattern += '(,\\s+(?P<description>.+))?\\]$'
        self.__entryRegex = re.compile(entryLinePattern)
    def begin(self):
        return None
    def end(self):
        # measure strings
        longest_code = 0
        for line in self.lines:
            entryMatch = self.__entryRegex.match(line)
            if (entryMatch):
                code_length = len(entryMatch.group('code'))
                if code_length > longest_code:
                    longest_code = code_length
        
        # create output
        output = ''
        for line in self.lines:
            entryMatch = self.__entryRegex.match(line)
            if (entryMatch):
                start = entryMatch.group('start')
                end = entryMatch.group('end')
                code = entryMatch.group('code')
                description = entryMatch.group('description')
                task = entryMatch.group('task')
                new_line = start
                new_line += '\t'
                if end:
                    new_line += end
                else:
                    new_line += '\t'
                new_line += '\t['
                new_line += code.ljust(longest_code, ' ')
                new_line += '\t'
                if task:
                    new_line += task
                if description:
                    new_line += task + ', ' 
                    new_line += description
                new_line += ']'
            else:
                new_line = line.strip()
            if output:
                output += '\n'
            output += new_line
        return output
