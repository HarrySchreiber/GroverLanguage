from grove_lang import *
import re

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

# Checking for string
def is_strlit(s):
    """ Takes a string and returns True if it is a string """

    return (s[0] == "\"" and s[len(s)-1] == "\"") and s.count("\"") == 2

def is_expr(x):
    if not isinstance(x, Expr):
        check(False, "Expected expression but found " + str(type(x)))

def is_name(x):
    pattern = r'[A-Za-z0-9_]+'
    if re.fullmatch(pattern, x) != None and (x[0].isalpha() or x[0] == "_"):
        return True

    return False

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
    #"call" "(" <Name> <Name> <Expr>* ")"
    elif start == "call":
        check(len(tokens) >= 5)
        expect(tokens[1], '(')
        check(is_name(tokens[2]), "Expected name, got " + tokens[2])
        check(is_name(tokens[3]), "Expected name, got " + tokens[3])
        expList = []
        endIndex = len(tokens)
        # keeps track of nested parenthesis
        nested = 0

        for i in range(4, len(tokens)-1):
            arg = tokens[i]
            if arg == ")":
                if nested == 0:
                    endIndex = i + 1
                    break
                else:
                    nested -= 1
            elif arg == "(":
                nested += 1
            expList.append(arg)

        if len(expList) > 0:
            val, remain = parse_tokens(expList)
            is_expr(val)
            expList = [val.eval()]
            while len(remain) > 0:
                val, remain = parse_tokens(remain)
                is_expr(val)
                expList.append(val.eval())

        return Call(Name(tokens[2]), Name(tokens[3]), expList), tokens[endIndex:]


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
    elif start == 'set':
        check(len(tokens) >= 4)
        check(is_name(tokens[1]), "Invalid Name: " + tokens[1])
        name = Name(tokens[1])
        expect(tokens[2], '=')
        # recursive match to parse expression
        expr, tokens = parse_tokens(tokens[3:])
        is_expr(expr)
        return Assignment(name, expr), tokens
    elif start == 'new':
        check(len(tokens) >= 2)
        return Object(tokens[1]), tokens[2:]
    elif start == 'import':
        check(len(tokens) >= 2)
        return Import(tokens[1]), tokens[2:]
    elif start == 'quit' or start == 'exit':
        return Terminate(), tokens[1:]
    elif is_name(start):
        return Name(start), tokens[1:]
    elif is_strlit(start):
        return StringLiteral(start[1:(len(start)-1)]), tokens[1:]
    else:
        check(False, "Unrecognized Command: " + start)

    # TODO: complete parser with cases for each possible type of command

    
# Informal Testing Code
if __name__ == "__main__":
    # TODO: Add some tests to check if your parser works properly (Optional)
    # root = parse("set f = new __builtins__.list")
    # root.eval()
    print(is_name("ab"))
    pass
