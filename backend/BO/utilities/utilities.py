from BO.helpers.relation import option_relation_dict
import json

class Utilities:
    def __init__(self):
        self.response = {
            'status': True,
            'message': ''
        }
        
    def list_genereic_options(self, option_list=[]):
        option_list = json.loads(option_list)
        
        for option in option_list:
            self.response[option + '_options'] = option_relation_dict[option]
            
        return self.response