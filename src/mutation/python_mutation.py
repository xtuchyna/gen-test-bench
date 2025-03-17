import os
import pandas as pd
from mutpy import utils
from mutpy.controller import MutationController

def run_mutation_tests(target, test):
    class Config:
        runner = 'unittest'
        timeout_factor = 5
        mutation_number = 0
        disable_stdout = False

    config = Config()
    controller = MutationController(
        target=target,
        tests=test,
        runner_name=config.runner,
        timeout_factor=config.timeout_factor,
        mutation_number=config.mutation_number,
        disable_stdout=config.disable_stdout
    )

    result = controller.run()
    return result

def process_directory(directory, df):
    target = os.path.join(directory, 'implementation.py')
    if not os.path.exists(target):
        print(f"No implementation.py found in {directory}")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith('test') and file.endswith('.py'):
                test_file = os.path.join(root, file)
                print(f"Running mutation tests for target: {target} with test: {test_file}")
                result = run_mutation_tests(target, test_file)
                relative_path = os.path.relpath(target, start=base_directory)
                df = df.append({
                    'index': relative_path,
                    'test_file': test_file,
                    'mutation_run': result
                }, ignore_index=True)
    return df

if __name__ == "__main__":
    base_directory = r'C:\Users\punksters\git\gen-test-bench\data\generated_passing'
    df = pd.DataFrame(columns=['index', 'test_file', 'mutation_run'])
    for root, dirs, _ in os.walk(base_directory):
        for dir in dirs:
            df = process_directory(os.path.join(root, dir), df)
    df.to_csv('mutation_results.csv', index=False)