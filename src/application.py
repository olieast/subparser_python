
class Application:
    def __init__(self):
        self.uc = 'client'

    def create_udeploy_application(self, args):
        print(args.token)
        print(args.yaml_file)

    def delete_udeploy_application(self, args):
        print(args.token)
        print(args.app_name)

