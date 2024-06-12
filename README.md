# Percolation Project

## Overview
This project simulates a percolation process using a grid-based approach. It generates a random grid of numbers and empty spaces, and outputs the results in both text and HTML formats. The project includes error handling and command-line interface for user input.

## Project Structure

- **perc.py**: The main program file that handles user input, initializes the process, and manages error handling.
- **Sub/Percolation.py**: Contains the core functionality for the percolation process.

## Requirements

- Python 3.x
- `prettytable` library: To install, use `pip install prettytable`

## Usage

### Running the Program

1. **Default Dimensions (5x5 Grid)**
   ```
   python perc.py
   ```

2. **Custom Dimensions**
   ```
   python perc.py NxM
   ```
   Replace `N` and `M` with integers between 3 and 9 to set the number of rows and columns.

### Example
To run a percolation simulation on a 4x4 grid:
```
python perc.py 4x4
```

### Output
The program generates:
- A text file with the grid and results
- An HTML file with a visual representation of the grid and results

## Functionality

### perc.py

1. **Imports necessary libraries and modules**.
   ```python
   import random
   import sys
   from prettytable import PrettyTable
   from datetime import datetime
   import Sub.Percolation
   ```

2. **Checks if the script is running in Python IDLE and exits if true**.
   ```python
   def check_idle():
       if "idlelib.run" in sys.modules:
           return True
       else:
           return False

   if check_idle():
       print("This script should be run in the command prompt, not in Python IDLE.")
       sys.exit(1)
   ```

3. **Handles errors and calls the main function from `Sub/Percolation.py`**.
   ```python
   try:
       Sub.Percolation.percolation_Function()
   except Exception as e:
       print("An error occurred:", e)
       sys.exit("Exiting due to error.")
   ```

### Sub/Percolation.py

1. **Generates a grid with random numbers and empty spaces**.
2. **Writes the grid to a text file and HTML file**.
3. **Provides OK/NO indicators based on the presence of numbers in columns**.
4. **Includes functions for writing to files, checking columns, and naming output files based on the current date and a random number**.

## Functions

### percolation_Function()
Generates the grid, writes to text and HTML files, and handles dimension inputs and errors.

### TextFileWriting()
Writes values of the grid to the text file.

### OKNO()
Prints OK or NO below the grid based on the contents of each column.

### NamingFiles()
Names the output files based on the current date and a random number.

## Example Output

### Text File
```
23 45 67
89 12 34
   56 78
OK OK NO
```

### HTML File
```html
<html>
<head>
<title>html.html</title>
</head>
<body>
<table style='border-collapse: collapse;'>
<tr><td style='border: 1px solid black; padding: 5px;'>23</td>
<td style='border: 1px solid black; padding: 5px;'>45</td>
<td style='border: 1px solid black; padding: 5px;'>67</td></tr>
<tr><td style='border: 1px solid black; padding: 5px;'>89</td>
<td style='border: 1px solid black; padding: 5px;'>12</td>
<td style='border: 1px solid black; padding: 5px;'>34</td></tr>
<tr><td style='border: 1px solid black; padding: 5px;'></td>
<td style='border: 1px solid black; padding: 5px;'>56</td>
<td style='border: 1px solid black; padding: 5px;'>78</td></tr>
<tr><td style='border: 1px solid black; padding: 5px;'>OK</td>
<td style='border: 1px solid black; padding: 5px;'>OK</td>
<td style='border: 1px solid black; padding: 5px;'>NO</td></tr>
</table>
</body>
</html>
```

## Error Handling

The program includes error handling to manage:
- Invalid dimension inputs
- Running the script in Python IDLE
- General execution errors

## Contributions

Feel free to contribute to this project by opening issues and submitting pull requests. Your feedback and improvements are welcome!

## License

This project is licensed under the MIT License.
