import pandas as pd

def convert_txt_to_csv():
    """
    Converts a .txt file to a .csv file and saves it.
    """
    txt_file_path = '/path/to/your/data'  # Path to the .txt file
    csv_file_path = '/path/to/your/data'  # Path where the .csv file will be saved
    
    try:
        # Read the .txt file into a DataFrame
        df = pd.read_csv(txt_file_path, delimiter="|")  # Adjust delimiter based on .txt file format
        # Save the DataFrame as a .csv file
        df.to_csv(csv_file_path, index=False)
        print(f"File successfully converted to {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def clean_csv():
    """
    Checks for missing values in the .csv file and removes rows with missing values.
    """
    csv_file_path = '/path/to/your/data'  # Path to the .csv file to be cleaned
    cleaned_csv_file_path = '/path/to/your/data'  # Path where the cleaned .csv file will be saved
    
    try:
        # Read the .csv file into a DataFrame
        df = pd.read_csv(csv_file_path)
        # Check for missing values
        missing_values = df.isnull().sum().sum()
        print(f"Total missing values: {missing_values}")
        
        # Remove rows with missing values
        df_cleaned = df.dropna()
        # Save the cleaned DataFrame as a new .csv file
        df_cleaned.to_csv(cleaned_csv_file_path, index=False)
        print(f"File successfully cleaned and saved to {cleaned_csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the functions to convert and clean the data
convert_txt_to_csv()
clean_csv()
