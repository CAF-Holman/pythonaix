import os

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
    # Will be True or False
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    # Check to see if accessing file is allowed
    if valid_target_file == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # Check to see if file_path points to an existing directory
    if os.path.isdir(target_file) == True:
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    # Make sure all parent directories of file_path exist
    os.makedirs(working_dir_abs, exist_ok=True)
    
    # Write to file
    try:
        with open(target_file, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        return f"Something fucked up!"

