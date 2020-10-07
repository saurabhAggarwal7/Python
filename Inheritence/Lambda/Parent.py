class ParentClass(object):
    def __init__(self, **kwargs):
        self.owner = kwargs.get('owner')
        
    def print_parent_status(self, payload_json):
        print(f'In Parent Class payload json recieved is {payload_json}')
        print(f'In Parent Class owner is {self.owner}')
