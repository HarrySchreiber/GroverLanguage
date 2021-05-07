## Parse tree nodes for the Calc language
## Note: Name and Statement will be the most different for GROVE language.
import re
import sys
import importlib
import builtins

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
	# TODO: Implement node for Number literals
	pass

class StringLiteral(Expr):
    # TODO: Implement node for String literals
    pass

class Object(Expr):
	# TODO: Implement node for "new" expression
    pass
    
class Call(Expr):
    # TODO: Implement node for "call" expression
    pass
        
class Addition(Expr):
    # TODO: Implement node for "+"
    pass

class Name(Expr):
    # TODO: Implement node for <Name> expressions
    pass

class Assignment(Stmt):
	# TODO: Implement node for "set" statements
	pass

class Import(Stmt):
    # TODO: Implement node for "import" statements
    pass

class Terminate(Stmt):
	# TODO: Implement node for "quit" and "exit" statements
	pass
        

# Informal Testing Code
if __name__ == "__main__":
	# TODO: Add some tests to check if your nodes work properly (Optional)
    pass

