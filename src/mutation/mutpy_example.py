import subprocess
import os
import pandas as pd

# TODO change for envvars
target_file = r'C:\Users\punksters\git\gen-test-bench\data\generated_passing\docs_python\associative_array_merging\implementation.py'
test_file = r'C:\Users\punksters\git\gen-test-bench\data\generated_passing\docs_python\associative_array_merging\test_deepseek_coder.py'

venv_python = r'C:\Users\punksters\.virtualenvs\gen-test-bench-zh5G7-DX\Scripts\python.exe'

def run_mutation(test_file, target_file):
    result = subprocess.run(
        ["python", "-m", "mutpy", "--unit-test", test_file, "--target", target_file],
        capture_output=True,
        text=True
    )
    return result

def process_directory(directory, df):
    target = os.path.join(directory, 'implementation.py')
    if not os.path.exists(target):
        print(f"No implementation.py found in {directory}")
        return df

    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith('test') and file.endswith('.py'):
                test_file = os.path.join(root, file)
                print(f"Running mutation tests for target: {target} with test: {test_file}")
                result = run_mutation(test_file, target)
                relative_path = os.path.relpath(target, start=base_directory)
                new_row = pd.DataFrame({
                    'index': [relative_path],
                    'test_file': [test_file],
                    'mutation_run': [result.stdout],
                    'error': [result.stderr]
                })
                df = pd.concat([df, new_row], ignore_index=True)
    return df

if __name__ == "__main__":
    base_directory = r'C:\Users\punksters\git\gen-test-bench\data\generated_passing'
    df = pd.DataFrame(columns=['index', 'test_file', 'mutation_run'])
    for root, dirs, _ in os.walk(base_directory):
        for dir in dirs:
            df = process_directory(os.path.join(root, dir), df)
    df.to_csv('mutation_results.csv', index=False)

