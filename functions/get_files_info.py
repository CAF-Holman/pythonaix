import os

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    rtn_message = ""
    
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs




    # Printing output header
    if directory == ".": # Specific exception for current directory
        rtn_message += f"Result for current directory: {directory} \n"

    else: # Catch all for all other directories
        rtn_message += f"Result for '{directory} directory:\n"

    # Check to see if accessing directory is allowed
    if valid_target_dir == False:
        rtn_message += f'   Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
        return rtn_message

    # Confirm target_dir is a directory
    try:
        file_list = os.listdir(target_dir)
    except:
        return f'Error: "{target_dir}" Not a Directory'

    for file in file_list:
        file_address = os.path.join(target_dir,file)
        if os.path.isdir(file_address) == True:
            rtn_message += f"   - {file}: file_size={os.path.getsize(file_address)}, is_dir={os.path.isdir(file_address)}\n"
        else:
            try:
                rtn_message += f"   - {file}: file_size={os.path.getsize(file_address)}, is_dir={os.path.isdir(file_address)}\n"
            except:
                print(f"Error: Inaccessable - {file}")
    return rtn_message

    
    
    
    
    
    
    


#f"{file_name}: file_size={file_size}, is_dir={is_a_dir}\n abso = {working_dir_abs}\n dir = {target_dir}"