import pandas as pd

def clean_employee_data(file_path, output_file):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df['Name'] = df['Name'].str.upper()
    df.to_csv(output_file, index=False)

# Example usage
clean_employee_data('employees.csv', 'cleaned_employees.csv')
