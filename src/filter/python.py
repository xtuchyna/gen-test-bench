import os
import subprocess

def is_python_file_runnable(filepath):
    try:
        result = subprocess.run(['python', filepath], capture_output=True, text=True, timeout=10)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"Timeout expired for {filepath}")
        return False
    except Exception as e:
        print(f"Error running {filepath}: {e}")
        return False

def rename_file(filepath):
    directory, filename = os.path.split(filepath)
    parent_directory = os.path.basename(directory)
    
    if 'test' in filename:
        new_filename = filename.replace(f"_{parent_directory}", "")
    elif filename == f"{parent_directory}.py":
        new_filename = "implementation.py"
    else:
        return  # No renaming needed

    new_filepath = os.path.join(directory, new_filename)
    os.rename(filepath, new_filepath)
    print(f"Renamed {filepath} to {new_filepath}")

def filter_python_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                if is_python_file_runnable(filepath):
                    rename_file(filepath)
                else:
                    print(f"Removing {filepath} as it cannot be run")
                    os.remove(filepath)


if __name__ == "__main__":
    directory = r'C:\Users\punksters\git\gen-test-bench\data\generated_passing\docs_python'
    filter_python_files(directory)