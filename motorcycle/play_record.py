import pyxel
from bitarray import bitarray
import base64
from world import *

class PlayRecord:
    def __init__(self, str_a = None, str_b = None):
        if str_a and str_b:
            self.set_str_a(str_a)
            self.set_str_b(str_b)
        else:
            self.reset()

    def reset(self):
        self.record_a = bitarray(endian='big')
        self.record_b = bitarray(endian='big')
        
    def add(self, a_pressed, b_pressed):
        if a_pressed:
            self.record_a.append(1)
        else:
            self.record_a.append(0)
        if b_pressed:
            self.record_b.append(1)
        else:
            self.record_b.append(0)
        tic = g_world.tic
        if len(self.record_a) != tic: raise
        if len(self.record_b) != tic: raise        

    def str_a(self):
        byte_data = self.record_a.tobytes()
        return base64.b64encode(byte_data).decode('utf-8')
    
    def str_b(self):
        byte_data = self.record_b.tobytes()
        return base64.b64encode(byte_data).decode('utf-8')

    def set_str_a(self, text):
        byte_data = base64.b64decode(text.encode('utf-8'))
        self.record_a = bitarray(endian='big')
        self.record_a.frombytes(byte_data)

    def set_str_b(self, text):
        byte_data = base64.b64decode(text.encode('utf-8'))
        self.record_b = bitarray(endian='big')
        self.record_b.frombytes(byte_data)
        
    def recorded_buttons(self, tic):
        if tic >= len(self.record_a):
            return [False, False]
        else:
            return [self.record_a[tic], self.record_b[tic]]
