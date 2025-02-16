import os
import json
from world import *

class Savedata:
    Directory = "savedata"
    TagTotal = "total"
    
    def __init__(self):
        self.filepath = False
        self.data = False

    def load(self):
        if not self.filepath:
            self.filepath = self.Directory + "/" + g_world.Version
        if not os.path.isfile(self.filepath):
            self.data = {}
            return
        try:
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)
        except json.JSONDecodeError:
            self.data = {}

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f)

    def set_time(self, tag, time):
        if not self.data:
            self.load()
        self.data[str(tag)] = time
        self.save()

    def time(self, tag):
        if not self.data:
            self.load()
        return self.data.get(str(tag), None)

g_savedata = Savedata()
