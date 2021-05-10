# TODO: Answer This Question
# Is your Grove interpreter using a static or dynamic type system? Briefly explain what aspects of the interpreter make it so.
# 
# 
# 

from grove_parse import *
from grove_lang import *

if __name__ == "__main__":
    while(True):
        root = parse(input("Grove>> "))
        result = root.eval()
        if(result != None):
            print(result)