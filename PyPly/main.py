# Import the necessary functions
from process_traceback import catch_all_errors, process_default_traceback

# Adjust the path to the Python script appropriately
script_path = r'C:\Users\mandy\Documents\Honours\Project\TNZMAN002_Final_Project_Code\PyPly\Tasks\FizzBuzz.py'

# Attempt to execute the submitted Python script and capture its output (including errors)
error = catch_all_errors(script_path)

if error is not None:
    try:
        # Allow the user to choose a language preference for error messages
        language = input("Enter E or X for language preference for error messages\n(E) English\n(X) isiXhosa\n").upper()
        
        # Try to process and improve/ translate the error message
        improved_error_message = process_default_traceback(error, language)
        print(improved_error_message)

    except Exception as e:
        # If there is an exception during the error processing, print the original error message
        print(error)

else:
    # Execute the script when there is no error
    exec(open(script_path).read())