import commandlineargumentexception

class CommandParser:
    def get_command(self, args):
        verb = self.__get_verb(args)        
        if verb.upper() in self.__class__.__name__.upper():
            command = self.fill_command(args)
        else:
            command = None
        return command

    def __get_verb(self, args):
        if len(args) < 2:
            message = 'Command not specified'
            raise commandlineargumentexception.CommandLineArgumentException(message) 
        return args[1]

class Command:
    def __init__(self):
        self.__input_path = '-'
        self.__output_path = '-'

    @property
    def input_path(self):
        return self.__input_path

    @input_path.setter
    def input_path(self, value):
        self.__input_path = value

    @property
    def output_path(self):
        return self.__output_path

    @output_path.setter
    def output_path(self, value):
        self.__output_path = value

class BufferedCommand(Command):
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