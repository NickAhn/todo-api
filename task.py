import json
'''
Task {
    "Text":task description
    "Priority": task priority
    "Complete": False
    "
}
'''
class Task:
    def __init__(self, text="", priority=4) -> None:
        if priority is None:
            priority = 4
        self.text = text
        self.priority = priority
        self.complete = False
    
    '''
    Return class attributes as a dictionary in json format
    '''
    def to_json(self) -> dict:
        dic = {
            "Text": self.text,
            "Priority": self.priority,
            "Complete": self.complete
        }
        return dic
