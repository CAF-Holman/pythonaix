import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    output_string = f""
    
    # Will be True or False
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    # Check to see if executing file is allowed
    if valid_target_file == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # Check to see if file path is acceptable
    if os.path.isfile(target_file) == False:
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    # Check to see if the file name ends with '.py'
    if file_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file'
    
    # Build command to execute
    command = ["python", target_file]

    # Add additional args
    if args != None:
        command.extend(args)

    # Run the command
    try:
        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30)

        if completed_process.returncode != 0:
            output_string += f"Process exited with code {completed_process.returncode}"

        if completed_process.stdout == None and completed_process.stderr == None:
            output_string += f"No output produced \n"
        else:
            output_string += f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
        
        return output_string
    
    except subprocess.TimeoutExpired as e:
        return f"Error: executing Python file: {e}"


