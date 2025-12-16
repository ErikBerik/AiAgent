import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        abs_wd_path = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
        if not (abs_file_path).startswith(abs_wd_path+os.path.sep):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS+1)
            if len(file_content_string) <= MAX_CHARS:
                return file_content_string
            else: 
                return file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f'Error: {e}'