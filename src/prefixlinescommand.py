import commandlineargumentexception
import commandparser

class PrefixLinesCommandParser(commandparser.CommandParser):
    def fill_command(self, args):
        if len(args) < 3:
            message = 'Prefix argument not specified'
            raise commandlineargumentexception.CommandLineArgumentException(message)
        command = PrefixLinesCommand()
        command.prefix = args[2]
        return command

class PrefixLinesCommand:
    def __init__(self):
        self.__prefix = ''
    @property
    def expects_input(self):
        return True
    @property
    def prefix(self):
        return self.__prefix
    @prefix.setter
    def prefix(self, value):
        self.__prefix = value
    def begin(self):
        return None
    def process(self, input):
        return self.prefix + input
    def end(self):
        return None
