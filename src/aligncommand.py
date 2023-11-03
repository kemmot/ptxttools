import os

import commandlineargumentexception
import commandparser

class AlignCommandParser(commandparser.CommandParser):
    def fill_command(self, args):
        if len(args) < 3:
            message = 'Delimiter argument not specified'
            raise commandlineargumentexception.CommandLineArgumentException(message)
        command = AlignCommand()
        command.separator = args[2]
        return command

class AlignCommand:
    def __init__(self):
        self.__separator = ': '
    @property
    def expects_input(self):
        return True
    @property
    def separator(self):
        return self.__separator
    @separator.setter
    def separator(self, value):
        self.__separator = value
    def init(self, args):
        if len(args) >= 3:
            self.__separator = args[2]
    def begin(self):
        self.__position = -1
        self.__lines = []
        return None
    def process(self, input):
        self.__lines.append(input)
        position = input.find(self.__separator)
        if position > self.__position:
            self.__position = position
        return None
    def end(self):
        output = ''
        for line in self.__lines:
            if len(output) > 0:
                #output += os.linesep
                output += '\n'
            parts = line.split(self.__separator)
            if len(parts) > 1:
                left = parts[0]
                right = parts[1]
                output += left.ljust(self.__position) + self.__separator + right
            else:
                output += line
        return output
