# Importing Python libraries.
import random
import sys
from prettytable import PrettyTable
from datetime import datetime

# Defining a function as percolation()

def percolation_Function():
    """ This function is used to get the dimension size from the user and create the table. And, this create the html and text file."""
    #Assigning the necessary variables as global to have the access out of the function.
    global row_values
    global fo
    global columns
    global row
    global html_table
    global grid
    global current_time
    global formatted_time
    global random_number
    global textfile
    global htmlfile

    try:

        
        # Variable initialization
        fo=0
        fo_html=0
        grid = []
        new1 = []
        new=[]
        rows=0
        row=0
        columns=0
        row_values=0
        random_number=0
        textfile=""
        htmlfile=""
        

        # Use try and except method to handle the exceptions.
        if len(sys.argv) == 1:
            # If no command-line arguments provided, set default dimensions to 5x5.
            rows = 5
            columns = 5
        elif len(sys.argv) == 2:
            # Getting the user input.
            val=sys.argv[1]
            # Use try and except method to handle the exceptions.
            try:
                # Extracting rows and columns from the user input.
                val1=val.split("x")
                rows = int(val1[0])
                columns = int(val1[1])
            except ValueError:
                d=("Value Error: Invalid dimensions.")
                print(d)
                sys.exit("Exiting due to invalid dimensions.")
        else:
            sys.exit(0)

                
        # Check whether rows and columns are between 3 and 9.
        if 3 <= rows <= 9 and 3 <= columns <= 9:

            #Using the function to name the files according to the format.
            NamingFiles()

            # Opening the text file.
            fo=open(textfile,"w")

            # Opening the html file.
            fo_html=open(htmlfile,"w")

            # Assigning prettytable format to the table variable.
            # header is False because we don't need header.
            # border,hrules,vrules are True as we need them for the table.
            table = PrettyTable(header=False, border=True, hrules=True, vrules=True)

            # Start to write the html code.
            # Assign it to html_table.
            # Add the other html codes to the html_table EX: html_table += "<table style='border-collapse: collapse;'>\n".
            html_table = "<html>\n<head>\n<title>html.html</title>\n</head>\n<body>\n"
            html_table += "<table style='border-collapse: collapse;'>\n"

            for i in range(rows):
                # Opening a new table row in html.
                html_table+="<tr>"
                # Empty these lists after each occurrence to add the data of the new occurrence.
                row_values = []
                new = []

                for j in range(columns):

                    # This generates a random float number between 0 and 1.
                    # There is a 80% probability to get a number.
                    # There is a 20% probability to get a " ".
                    if random.random() > 0.2:
                        # Getting a random number between 10 and 99 because in the specification, it is mentioned to get two digits numbers.
                        rand1 = random.randint(10, 99)
                        # Add data for the table row.
                        # Border style is changed according to our preference. 
                        html_table += f"<td style='border: 1px solid black; padding: 5px;'>{rand1}</td>"

                        # Appending the data to the row_values list.
                        row_values.append(rand1)
                        new.append('OK')
                    else:
                        # Add data for the table row.
                        # Border style is changed according to our preference.
                        html_table += f"<td style='border: 1px solid black; padding: 5px;'></td>"
                        row_values.append(" ")
                        new.append('NO')

                # Appending the row_values list to the grid list as row_values list becomes empty in the next loop.
                grid.append(row_values)

                # Add a new row for html.
                html_table += "</tr>"

                # Calling the function,TextFileWriting() to write row_values to the textfile.
                TextFileWriting()
                
                # Goes to the next line in text file.
                fo.write("\n")

                # Append the list to the another list to store the data in that list.
                new1.append(new)
                # Adding row to the table.
                table.add_row(row_values)

            # Display the table.
            print(table)

            # Adding new row and next line to the  htmlfile.
            html_table += "</tr>"

            # Print OK if all the data in column is numbers.
            # Print NO if the column contains " ".

            OKNO()

            # Closing the table and html.
            html_table += "</tr>\n</table>\n</body>\n</html>"

            # Write html_table to html file.
            fo_html.write(html_table)

            # Closing the files.
            fo.close()
            fo_html.close()
        else:
            raise ValueError("Dimensions should be between 3x3 and 9x9.")
            
    except Exception as e:
        print("An error occurred:", e)
        sys.exit("Exiting due to error.")
        
    return
    
#Defining a function called TextFileWriting.
def TextFileWriting():
    """ This function is used to write the values of the grid to the text file. """
    #Assigning the variables as global.
    global row_values
    global fo

    for v in row_values:
        if v==" ":
            fo.write("  ")
            fo.write(" ")
        else:
            fo.write(str(v))
            fo.write(" ")
    

#Defining a function called YesNo.
def OKNO():
    """ This function is used to print OK or NO below the grid by checking it. """
    #Assigning the variables as global.
    global columns
    global row
    global html_table
    global fo
    global grid
    
    for col in range(columns):
        if all(row[col] != " " for row in grid):
            # Add data for the table row.
            # Border style is changed according to our preference. 
            html_table += f"<td style='border: 1px solid black; padding: 5px;'>OK</td>"
            print("  OK",end=" ")

            # Writing to the text file.
            fo.write("OK ")
        else:
            print("  NO",end=" ")
            # Add data for the table row.
            # Border style is changed according to our preference. 
            html_table += f"<td style='border: 1px solid black; padding: 5px;'>NO</td>"

            # Writing to the text file
            fo.write("NO ")

#Defining a function called NamingFiles.
def NamingFiles():
    """ This function is used to Name the files according to the date."""
    #Assigning the variables as global.
    global current_time
    global formatted_time
    global random_number
    global textfile
    global htmlfile

    
    
    # Using datetime module to assign the filename.
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y_%m_%d")
    random_number = random.randint(1000, 9999)
    textfile = f"{formatted_time}_{random_number}.txt"
    htmlfile = f"{formatted_time}_{random_number}.html"

    return
