import argparse, sys
from command_manager import CommandManager

def main(argv):

    # Create the top-level parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', dest='token', help='auth token')

    # Add subparsers
    subparsers = parser.add_subparsers(help='sub-command help')
    command_manager = CommandManager()
    for command in command_manager.commands:
        subparse = subparsers.add_parser(command)
        command_manager.register_arguments(subparse, command)
        subparse.set_defaults(func=command_manager.execute, command=command)

    args = parser.parse_args(argv)
    args.func(args, args.command)

if __name__ == '__main__':
    main(sys.argv[1:])

    # python cli.py -t=token create-udeploy-application -f=./file.yml
    # python cli.py -t=token delete-udeploy-application -name=app_name_uu


