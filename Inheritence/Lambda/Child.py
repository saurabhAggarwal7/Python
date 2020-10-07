class Child(git.Parent):

    #Pass on Keyword arguments to parent class GitAPP
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def print_child_status(self):
        payload_json = {'test': '123'}
        super().print_parent_status(payload_json)

def lambda_handler(event, context):
    child_obj = Child(owner='owner-1')
    child_obj.print_child_status()
