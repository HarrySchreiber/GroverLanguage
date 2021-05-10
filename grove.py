# Is your Grove interpreter using a static or dynamic type system? Briefly explain what aspects of 
# the interpreter make it so.
# 
# The Grove interpreter is dynamically typed. When defining variables or just evaluating types
# the interpreter already knows what the type the value is of and we can change its type dynamically.
# We also do not need to tell the interpreter what type a variable is before we assign it. For these 
# reasons we know that our interpreter is dynamically typed.

from grove_parse import *
from grove_lang import *

if __name__ == "__main__":
    while(True):
        root = parse(input("Grove>> "))
        result = root.eval()
        if(result != None):
            print(result)