## Parse tree nodes for the Calc language
## Note: Name and Statement will be the most different for GROVE language.
import re
import sys
import importlib
import builtins

var_table = {}

# The exception class from the notes.
class GroveError(Exception):
    pass

# Command Base Class (superclass of expressions and statements)
class Command(object):
    pass

# Expression Base Class (superclass of Num, Name, StringLiteral, etc.)
class Expr(Command):
    pass

# Statement Base Class (superclass of Assign, Terminate, and Import)
class Stmt(Command):
    pass

# -----------------------------------------------------------------------------
# Implement each of the following parse tree nodes for the Grove language
# -----------------------------------------------------------------------------

class Num(Expr):
    def __init__(self, val):
        self.val = val
    def eval(self):
        return self.val

class StringLiteral(Expr):
    def __init__(self,val):
        self.val = val
    def eval(self):
        return self.val
    pass

class Object(Expr):
	# TODO: Implement node for "new" expression
    def __init__(self, val):
        self.val = val
    def eval(self):
        try:

            if("." not in self.val):
                if self.val == "GroveError":
                    return GroveError()

            parts = self.val.split(".")
            container = globals()[parts[0]]

            if isinstance(container, dict):
                cls = container[parts[1]]
            else:
                cls = getattr(container, parts[1])
            return cls()
        except Exception:
            raise GroveError("GROVE: No object with that module") 
    
class Call(Expr):
    # TODO: Implement node for "call" expression
    def __init__(self, name1, name2, args):
        self.name1 = name1
        self.name2 = name2
        self.args = args

    def eval(self):
        #TODO: figure out what goes here
        if(self.name1 in globals() or str(self.name1) in var_table.keys()):
            if(self.name2 in dir(self.name2) or str(self.name1) in var_table.keys()):
                try:
                    method = getattr(self.name1.eval(), str(self.name2))
                    return method(*self.args)
                except:
                    raise GroveError("GROVE: No method with name: " + str(self.name2))
            else:
                raise GroveError("GROVE: No method with name: " + str(self.name2))
        else:
            raise GroveError("GROVE: No Object with name: " + str(self.name1))
        
class Addition(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        if type(self.left.eval()) == type(self.right.eval()):
            return self.left.eval() + self.right.eval()
        else:
            raise GroveError("Grove: Addition must be between values of the same type")

class Name(Expr):
    # TODO: Implement node for <Name> expressions
    def __init__(self, val):
        self.val = val
    def eval(self):
        if(self.val in var_table):
            return var_table[self.val]
        else:
            raise GroveError("GROVE: No Value for variable with name: " + self.val)

    def __str__(self):
        return self.val

class Assignment(Stmt):
	# TODO: Implement node for "set" statements
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    def eval(self):
        val = self.expr.eval()
        var_table[self.name.val] = val
        return None

class Import(Stmt):
    def __init__(self, val):
        self.val = val
    def eval(self):
        try:
            lib = importlib.import_module(self.val)
            globals()[self.val] = lib
        except(Exception):
            raise GroveError("GROVE: No module with name: " + self.val)
        return None

class Terminate(Stmt):
	# TODO: Implement node for "quit" and "exit" statements
    def __init__(self):
        pass
    def eval(self):
        sys.exit()
        return None
        

# Informal Testing Code
if __name__ == "__main__":
	# TODO: Add some tests to check if your nodes work properly (Optional)
    pass

