import ply.lex as lex

# Token list
tokens = (
    'TYPE',
    'VARIABLE',
    'FUNCTION',
    'OPERATOR',
    'NUMBER',
    'STANDARD_INFO',
    'VALUE',
    'ERROR_TYPE',
    'SUGGESTION',
)

# Token regex patterns
t_VARIABLE = r"(?<!\w)'([^']+)'(?!\w)"  # Matches single-quoted strings
t_TYPE = r"(?<![^\s:])\b(?:'?(?:string|str|int|float|complex|bool|bytes|list|tuple|set|dict|integer|boolean|dictionary)'?)(?=(?:[\s:]|$))"  # Matches Python type names
t_FUNCTION = r"\w+\(\)"  # Matches function calls
t_OPERATOR = r"(?<=\s)(\+|\-|\/\/|\/|\*\*|\*|\^|%|\+=|\>|\<|\<=|\>=|'<'|'>'|'<='|'>='|&)(?=\s|:)"  # Matches operators
t_STANDARD_INFO = r"File\s\"([^']*)\",\sline\s(\d+)(\sin\s<\w+>)?.*?(\n.*)"  # Matches standard information: Filename, line and the offending line in tracebacks
t_VALUE = t_VALUE = r"'([-+]?(\d{1,3}(?:\s\d{3})*|\d*\.?\d+))'"  # Matches numeric values in single quotesS
t_SUGGESTION = r"\.([^.!?]*[.!?])"  # Matches suggestions
t_ERROR_TYPE = r"(\w+(?:Error|Warning)):"  # Matches error or warning types

# Ignored characters (whitespace and tabs)
t_ignore = ' \t'

# Handles newline characters and increments the line number for tracking in the lexer
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a custom t_NUMBER token, which matches digits and converts the value to an integer
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a custom t_SINGLE_QUOTED_TYPE token to capture single-quoted Python type names as TYPE tokens
def t_QUOTED_TYPE(t):
    r'(\'(int|float|complex|bool|str|bytes|list|tuple|set|dict|integer|boolean|string|dictionary)\'|\"(int|float|complex|bool|str|bytes|list|tuple|set|dict|integer|boolean|string|dictionary)\")'
    t.type = 'TYPE'
    t.value = t.value[1:-1]  # Remove the enclosing quotes
    return t

def t_error(t):
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
