import os
import json
import pyxel
from world import *

# reference: https://note.com/frenchbread/n/n9a46ada3850e
IsWeb = True
try:
    from js import window
except:
    IsWeb = False

class Savedata:
    TagTotal = "total"
    
    def __init__(self):
        self.filepath = False
        self.storage_item = False
        self.data = False

    def load(self):
        try:
            if IsWeb:
                self.storage_item = "bumping_rinder_savedata_" + g.world.Version
                data_str = window.localStorage.getItem(self.storage_item)
            else:
                dir = pyxel.user_data_dir("Sasakiki", "Bumping Rider")
                if not self.filepath:
                    self.filepath = dir + "savedata_" + g_world.Version
                    print(self.filepath)
                    if not os.path.isfile(self.filepath):
                        self.data = {}
                        return
                with open(self.filepath, 'r') as f:
                    data_str = f.read()
            self.data = json.load(data_str)
        except Exception:
            self.data = {}

    def save(self):
        try:
            data_str = json.dumps(self.data)
            if IsWeb:
                window.localStorage.setItem(self.storage_item, data_str)
            else:
                with open(self.filepath, 'w') as f:
                    f.write(data_str)
        except Exception:
            pass

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
