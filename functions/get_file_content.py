import os

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    rtn_message = ""
    
    # Will be True or False
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs


    # Check to see if accessing file is allowed
    if valid_target_file == False:
        rtn_message += f'Error: Cannot read "{file_path}" as it is outside the permitted working directory\n'
        return rtn_message
    
    # Check to see if file_path is a file
    if os.path.isfile(target_file) == False:
        rtn_message += f'Error: File not found or is not a regular file: "{file_path}\n'
        return rtn_message
    
    # Set maximum amout of characters to read from file
    max_chars = 10000

    # Read from file
    with open(target_file, "r") as file:
        file_content = file.read(max_chars)
        fc2 = file.read()
        if len(fc2) > max_chars:
            file_content += f'[...File "{file_path}" truncated at {max_chars} characters]'

    rtn_message += file_content

    # Return the message and complete the function
    return rtn_message
