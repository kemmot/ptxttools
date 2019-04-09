import commandlineargumentexception

class CommandFactory:
    def __init__(self):
        self.__commands = []

    def register(self, command):
        self.__commands.append(command)

    def get_command(self, args):
        verb = self.get_verb(args)
        for command in self.__commands:
            if verb.upper() in command.__class__.__name__.upper():
                return command

        message = 'Unknown command: {}'.format(verb)
        raise commandlineargumentexception.CommandLineArgumentException(message)

    def get_verb(self, args):
        if len(args) < 2:
            message = 'Command not specified'
            raise commandlineargumentexception.CommandLineArgumentException(message) 

        return args[1]
