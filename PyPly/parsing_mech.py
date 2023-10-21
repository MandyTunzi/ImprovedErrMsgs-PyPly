import ply.yacc as yacc
import re
from lexing_mech import tokens, lexer

# Grammar rules
def p_message(p):
    '''
    message : message element
             | element
    '''
    # Rule to represent a message with multiple elements or a single element
    # Concatenates the parsed elements to form the message
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_element(p):
    '''
    element : VARIABLE 
            | TYPE
            | FUNCTION
            | OPERATOR
            | NUMBER
            | STANDARD_INFO
            | VALUE
            | SUGGESTION
            | ERROR_TYPE
    '''

    # Rule for each element type
    # Calls specific handlers for each type of element to extract relevant information
    # and form a list of tuples representing the element and its tag
    handlers = {
        'VARIABLE': handle_var,
        'TYPE': handle_type,
        'FUNCTION': handle_func,
        'STANDARD_INFO': handle_standard_info,
        'VALUE': handle_value,
        'SUGGESTION': handle_suggestion,
        'ERROR_TYPE': handle_error_type
    }
    element_type = p.slice[1].type
    p[0] = handlers.get(element_type, handle_default)(p[1], element_type)

# Handlers for different element types
def handle_var(value, element_type):
    # Handler for VARIABLE elements (single-quoted strings)
    match = re.search(r"(?<!\w)'([^']+)'(?!\w)", value)  # Match single-quoted strings
    if match:
        return [(match.group(1), element_type)]
    return []

def handle_type(value, element_type):
    # Handler for TYPE elements (Python type names)
    match = re.search(r"(?<![^\s:])\b(?:'?(?:string|str|int|float|complex|bool|bytes|list|tuple|set|dict|integer|boolean|dictionary)'?)(?=(?:[\s:]|$))", value)  # Match Python type names
    if match:
        return [(match.group(0), element_type)]
    return []

def handle_func(value, element_type):
    # Handler for FUNCTION elements (function calls)
    match = re.search(r"\w+\(\)", value)  # Match function calls
    if match:
        return [(match.group(0), element_type)]
    return []

def handle_value(value, element_type):
    # Handler for VALUE elements (numeric values)
    match = re.search(r"'([-+]?(\d{1,3}(?:\s\d{3})*|\d*\.?\d+))'"
, value)  # Match numeric values
    if match:
        return [(match.group(1), element_type)]
    return []

def handle_error_type(value, element_type):
    # Handler for ERROR_TYPE elements (error or warning types)
    match = re.search(r"(\w+(?:Error|Warning)):", value)  # Match error or warning types
    if match:
        return [(match.group(1), element_type)]
    return []

def handle_suggestion(value, element_type):
    # Handler for SUGGESTION elements (suggestions)
    match = re.search(r"\.([^.!?]*[.!?])", value)  # Match suggestions
    if match:
        return [(match.group(1), element_type)]
    return []

def handle_default(value, element_type):
    # Default handler for elements that do not match any specific type
    if isinstance(value, int):
        value = str(value)
    return [(value, element_type)]

def handle_standard_info(value, element_type):
    # Handler for STANDARD_INFO elements (FILENAME, LINENUMBER and OFFENDING_LINE)
    lines = value.split("\n")
    info = []

    for i in range(len(lines)):
        if i % 2 == 0:
            line = lines[i]
            next_line = lines[i+1] if i+1 < len(lines) else None
            match = re.search(r'File\s"([^"]+)",\sline\s(\d+)', line)  # Extract filename and line number from standard info line
            if match and next_line:
                filename = match.group(1)
                line_number = int(match.group(2))
                offending_line = next_line.strip()
                info.append((filename, 'FILENAME'))
                info.append((line_number, 'LINENUMBER'))
                info.append((offending_line, 'OFFENDING_LINE'))

    return info

def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
