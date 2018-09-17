from application import Application

class Command:
    CREATE_UDEPLOY_APPLICATION = 'create-udeploy-application'
    DELETE_UDEPLOY_APPLICATION = 'delete-udeploy-application'
    CREATE_UDEPLOY_ENVIRONMENT = 'create-udeploy-environment'

class CommandManager:
    def __init__(self):
        commands = []
        commands.append(Command.CREATE_UDEPLOY_APPLICATION)
        commands.append(Command.DELETE_UDEPLOY_APPLICATION)
        commands.append(Command.CREATE_UDEPLOY_ENVIRONMENT)
        self.commands = commands

    def register_arguments(self, parser, command):
        if command == Command.CREATE_UDEPLOY_APPLICATION:
            parser.add_argument('-f', dest='yaml_file', type=str, help='yaml file path')
        elif command == Command.DELETE_UDEPLOY_APPLICATION:
            parser.add_argument('-name', dest='app_name', type=str, help='uDeploy application name')
        elif command == Command.CREATE_UDEPLOY_ENVIRONMENT:
            pass
        else:
            print('Not valid command')
            print(command)

    def execute(self, args, command):
        if command == Command.CREATE_UDEPLOY_APPLICATION:
            app = Application()
            app.create_udeploy_application(args)
        elif command == Command.DELETE_UDEPLOY_APPLICATION:
            app = Application()
            app.delete_udeploy_application(args)
        elif command == Command.CREATE_UDEPLOY_ENVIRONMENT:
            pass
        else:
            print('Not valid command')
            print(command)


