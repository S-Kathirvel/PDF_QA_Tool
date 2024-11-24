import pandas as pd
from tkinter import filedialog, Tk

def process_csv_file(file_path):
  """
  Processes a single CSV file.

  Args:
      file_path (str): Path to the CSV file.

  Returns:
      pandas.DataFrame: The loaded DataFrame or None if there's an error.
  """
  try:
    df = pd.read_csv(file_path)
    print(f"Successfully processed file: {file_path}")
    return df
  except Exception as e:
    print(f"Error parsing {file_path}: {str(e)}")
    return None

def select_file():
  """
  Opens a file selection dialog and returns the selected file path.
  """
  root = Tk()
  root.withdraw()  # Hide the main window
  file_path = filedialog.askopenfilename(title="Select CSV File")
  return file_path

# Get CSV file path using file dialog
file_path = select_file()

# Process the CSV file
if file_path:
  df = process_csv_file(file_path)
  # Do something with the DataFrame (if processing was successful)
  if df is not None:
    # Your logic to analyze or utilize the DataFrame 'df' goes here
    print("Here's a glimpse of the data:")
    # print(df.head())  # Display the first few rows

print("Data is retrieved")
