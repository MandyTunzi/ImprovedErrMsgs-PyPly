import traceback
import sqlite3
from parsing_mech import parser, lexer 
import subprocess
import os
import sys

# Connect with database
dbase = sqlite3.connect('error_msg.db')
cursor = dbase.cursor()

# Catch the deafult error message present in a given Python script
def catch_all_errors(filename):
    try:
        # Get the full path of the current script
        script_directory = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path of the input file using its filename
        file_path = os.path.join(script_directory, filename)
        
        python_executable = sys.executable
        result = subprocess.run([python_executable, file_path], capture_output=True, text=True)
        if result.returncode != 0:
            # If the return code is non-zero, there was an error in the executed code
            error_message = result.stderr
          #  parse_error(error_message)
            return error_message
        else:
            # Code executed successfully
            output = result.stdout
            return None
    except Exception as e:
        full_traceback = traceback.format_exception(type(e), e, e.__traceback__)
        joined_traceback = "".join(full_traceback)
        return joined_traceback


# Extract all the error-specific information from original traceback
def extract_elements(message):
    # Check if the input message is empty or contains only whitespace
    if not message or len(message.strip()) == 0:
        return None
    
    # Use the parser to parse the message and extract elements with tags
    elements = parser.parse(message, lexer=lexer)

    # If the parser returns None, there are no elements to extract
    if elements is None:
        return None

    # Extract individual elements and their corresponding tags
    output_elements = []
    for element, tag in elements:
        output_elements.append((element, tag))

    # Return the list of extracted elements with tags
    return output_elements


# Create a template of the original error message traceback(with placeholders where elements have been extracted). 
def generate_template(element_list, input_trace):
    if element_list is not None:
        temp = input_trace
        for element, tag in element_list:
           # print(f"{tag}: {element}")
            temp = temp.replace(str(element), f"[{str(tag)}]")
        return temp
    

# Replace placeholders in the template with corresponding values from lists
def generate_traceback(template, data_list):
    # Create a dictionary to hold all occurrences of each key as a list
    data_dict = {}
    for value, key in data_list:
        data_dict.setdefault(key, []).append(value)

    # Replace placeholders in the template with corresponding values from lists
    for key, values in data_dict.items():
        placeholder = f"[{key}]"
        for value in values:
            template = template.replace(placeholder, str(value), 1)
            
    return template


# Initial processing of error message traceback
def clean_input(input_string):
    lines = input_string.strip().split('\n')
    
    # Check for specific error types
    error_types = ["SyntaxError", "IndentationError", "TabError"]
    for error_type in error_types:
        if any(line.startswith(error_type) for line in lines):
            lines.pop(-2)  # Remove second last line
            return '\n'.join(lines[-3:])  # Return last three lines
    num_lines = len(lines)
    if num_lines > 4:
        return '\n'.join(lines[-3:])
    elif num_lines == 4:
        if lines[0].startswith("Traceback"):
            lines.pop(0)
            return '\n'.join(lines)
        else:
            lines.pop(2)
            return '\n'.join(lines)
    
    return '\n'.join(lines)


# Fetch the improved template for the error message
def fetch_improved_template(MESSAGE):
    # Execute a SELECT query to fetch the new template for the given default MESSAGE template
    cursor.execute("SELECT IMPROVED_TEMPLATE FROM error_message_info WHERE DEFAULT_TEMPLATE=?", (MESSAGE,))

    # Fetch the result
    result = cursor.fetchone()

    # Return the improved error message template
    return result[0]


# Fetch the improved template for the error message
def fetch_translated_template(MESSAGE):
    # Execute a SELECT query to fetch the translated template for the given default MESSAGE template
    cursor.execute("SELECT TRANSLATED_TEMPLATE FROM error_message_info WHERE DEFAULT_TEMPLATE=?", (MESSAGE,))

    # Fetch the result
    result = cursor.fetchone()

    # Return the translated error message
    return result[0]


# Generate improved translated error message
def process_default_traceback(input_trace, language):
    clean_input_trace = clean_input(input_trace)
    output_elements = extract_elements(clean_input_trace.strip(" "))

    default_template = generate_template(output_elements, clean_input_trace)
    improved_template = fetch_improved_template(default_template.replace('"', '').split('\n')[2])
    translated_template = fetch_translated_template(default_template.replace('"', '').split('\n')[2])

    if language == 'E':
        formatted_traceback = generate_traceback(improved_template, output_elements)
    elif language == 'X':
        formatted_traceback = generate_traceback(translated_template, output_elements)

    return formatted_traceback.replace("\\n", "\n")
