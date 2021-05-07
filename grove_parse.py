from grove_lang import *

# Utility methods for handling parse errors
def check(condition, message = "Unexpected end of expression"):
    """ Checks if condition is true, raising a ValueError otherwise """
    if not condition:
        raise GroveError("GROVE: " + message)
        
def expect(token, expected):
    """ Checks that token matches expected
    If not, throws a ValueError with explanatory message """
    check(token == expected, "Expected '" + expected + "' but found '" + token + "'")
       
def parse(s):
    """ Return an object representing a parsed command
        Throws ValueError for improper syntax """
    (root, remaining_tokens) = parse_tokens(s.split())
    check(len(remaining_tokens) == 0, "Expected end of command but found " + " ".join(remaining_tokens))    
    return root

#TODO: Are these supposed to be in here?
# Checking for integer        
def is_int(s):
    """ Takes a string and returns True if in can be converted to an integer """
    try:
        int(s)
        return True
    except Exception:
        return False

def is_expr(x):
    if not isinstance(x, Expr):
        check(False, "Expected expression but found " + str(type(x)))

# -----------------------------------------------------------------------------
# Implement the recursive parser for the Grove language
# -----------------------------------------------------------------------------

def parse_tokens(tokens):
    """ Returns a tuple:
        (an object representing the next part of the expression,
         the remaining tokens)
    """
    
    check(len(tokens) > 0)
        
    start = tokens[0]

    if is_int(start):
        return Num(int(start)), tokens[1:]
    elif start == '+':
        check(len(tokens) >= 7)
        expect(tokens[1], '(')
        # recursively parse right expression
        left, tokens = parse_tokens(tokens[2:])
        is_expr(left)
        expect(tokens[0], ')')
        expect(tokens[1], '(')
        # recursively parse right expression
        right, tokens = parse_tokens(tokens[2:])
        is_expr(right)
        expect(tokens[0], ')')
        return Addition(left, right), tokens[1:]
    else:
        check(False, "Unrecognized Command: " + start)

    # TODO: complete parser with cases for each possible type of command

    
# Informal Testing Code
if __name__ == "__main__":
    # TODO: Add some tests to check if your parser works properly (Optional)
    pass
