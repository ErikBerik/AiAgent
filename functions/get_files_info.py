import os

def get_files_info(working_directory, directory="."):
    target_path = os.path.join(working_directory, directory)
    abs_target_path = os.path.abspath(target_path)
    abs_wd_path = os.path.abspath(working_directory)
    if (abs_target_path).startswith(abs_wd_path+os.path.sep) or abs_target_path==abs_wd_path:
        if os.path.isdir(abs_target_path):
            try:
                content_list = os.listdir(abs_target_path)
                lines = []
                for entry in content_list:
                    entry_path = os.path.join(abs_target_path,entry)
                    filesize = os.path.getsize(entry_path)
                    isdir = os.path.isdir(entry_path)
                    line = f"- {entry}: file_size={filesize} bytes, is_dir={isdir}"
                    lines.append(line)
                return "\n".join(lines)
            except Exception as e:
                return f'Error: {e}'
        else:
            return f'Error: "{directory}" is not a directory'
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
