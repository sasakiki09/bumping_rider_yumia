import os
import json
import pyxel
from world import *

class Savedata:
    Directory = False
    TagTotal = "total"
    
    def __init__(self):
        self.filepath = False
        self.data = False

    def load(self):
        if not Savedata.Directory:
            Savedata.Directory = pyxel.user_data_dir("Sasakiki", "Motorcycle Yumia")
        if not self.filepath:
            self.filepath = Savedata.Directory + "savedata_" + g_world.Version
            print(self.filepath)
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
