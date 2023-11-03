import commandlineargumentexception

class CommandFactory:
    def __init__(self):
        self.__command_parsers = []

    def register(self, command_parser):
        self.__command_parsers.append(command_parser)

    def get_command(self, args):
        for command_parser in self.__command_parsers:
            command = command_parser.get_command(args)
            if command != None:
                return command
        message = 'Unknown command: {}'.format(args[1])
        raise commandlineargumentexception.CommandLineArgumentException(message)

