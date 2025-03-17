import os
import pandas as pd
import io
import sys
from contextlib import redirect_stdout
import mutpy.controller as controller
import mutpy.views as views
import mutpy.operators as operators
import mutpy.utils as utils

# Custom view to capture mutation results
class CaptureOutputView(views.QuietTextView):
    def __init__(self):
        super().__init__()
        self.output = io.StringIO()
        
    def write(self, message):
        self.output.write(message)
        
    def get_output(self):
        return self.output.getvalue()

# Function to run MutPy on a given implementation file and test file
def run_mutation(implementation_path, test_path):
    # Create a view to capture output
    capture_view = CaptureOutputView()
    
    # Configure MutPy
    configuration = utils.Config(
        target_path=implementation_path,
        test_path=test_path,
        runner_path=None,
        mutation_number=None,
        operators_string=None,
        show_mutants=False,
        quiet_mode=False,
        disable_stdout=False,
        timeout_factor=5,
        run_directory=os.path.dirname(implementation_path),
    )
    
    # Initialize the controller
    mutation_controller = controller.MutationController(
        runner_cls=utils.get_runner(configuration.runne r),
        target_loader=utils.get_target_loader(configuration.target),
        test_loader=utils.get_test_loader(),
        views=[capture_view],
        mutant_generator=operators.get_mutator(configuration),
    )
    
    # Run mutation testing and capture output
    with redirect_stdout(io.StringIO()):  # Suppress stdout
        mutation_controller.run()
    
    return capture_view.get_output()

# Function to find all implementation.py files and their test files
def find_implementation_and_test_files(root_dir):
    implementation_test_pairs = []
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Check if implementation.py exists in this directory
        if 'implementation.py' in filenames:
            implementation_path = os.path.join(dirpath, 'implementation.py')
            
            # Find all test files in the same directory
            test_files = [f for f in filenames if f.startswith('test') and f.endswith('.py')]
            
            if test_files:
                for test_file in test_files:
                    test_path = os.path.join(dirpath, test_file)
                    implementation_test_pairs.append((implementation_path, test_path))
            
    return implementation_test_pairs

# Main function
def main():
    root_dir = r'C:\Users\punksters\git\gen-test-bench\data\generated_passing'  # Adjust path format based on OS
    
    # Find all implementation.py files and their test files
    print(f"Searching for implementation.py files in {root_dir}...")
    implementation_test_pairs = find_implementation_and_test_files(root_dir)
    print(f"Found {len(implementation_test_pairs)} implementation-test pairs.")
    
    # Create DataFrame to store results
    results_df = pd.DataFrame(columns=['test_file', 'mutation_run'])
    
    # Run mutation testing for each pair and add to DataFrame
    for i, (implementation_path, test_path) in enumerate(implementation_test_pairs):
        print(f"Running mutation {i+1}/{len(implementation_test_pairs)}: {implementation_path} with {test_path}")
        
        try:
            # Run mutation testing
            mutation_output = run_mutation(implementation_path, test_path)
            
            # Get relative path for implementation file (to use as index)
            rel_implementation_path = os.path.relpath(implementation_path, start=os.getcwd())
            rel_test_path = os.path.relpath(test_path, start=os.getcwd())
            
            # Add result to DataFrame
            results_df.loc[rel_implementation_path, 'test_file'] = rel_test_path
            results_df.loc[rel_implementation_path, 'mutation_run'] = mutation_output
            
            print(f"Completed mutation testing for {rel_implementation_path}")
        except Exception as e:
            print(f"Error running mutation for {implementation_path}: {str(e)}")
    
    # Save DataFrame to CSV
    csv_path = 'mutation_results.csv'
    results_df.to_csv(csv_path)
    print(f"Results saved to {csv_path}")
    
    # Save DataFrame to Excel for better handling of large text in cells
    excel_path = 'mutation_results.xlsx'
    results_df.to_excel(excel_path)
    print(f"Results also saved to {excel_path}")
    
    # Print summary
    print(f"\nMutation Testing Summary:")
    print(f"Total implementation files tested: {len(results_df)}")
    
    return results_df

if __name__ == "__main__":
    results = main()