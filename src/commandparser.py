import commandlineargumentexception

class CommandParser:
    def get_command(self, args):
        verb = self.__get_verb(args)
        if verb.upper() in self.__class__.__name__.upper():
            return self.fill_command(args)
        else:
            return None

    def __get_verb(self, args):
        if len(args) < 2:
            message = 'Command not specified'
            raise commandlineargumentexception.CommandLineArgumentException(message) 
        return args[1]

class BufferedCommand:
    def __init__(self):
        self.__lines = []
    @property
    def expects_input(self):
        return True
    @property
    def lines(self):
        return self.__lines
    def process(self, input):
        self.__lines.append(input)
        return None