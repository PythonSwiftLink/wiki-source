#hello_world.py
from swift_tools.swift_types import *

@wrapper
class HelloWorld:

    def send_string(self, string: str): ...
        
