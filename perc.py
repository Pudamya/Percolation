# Main programme.

#Import the Python Libraries.
import random
import sys
from prettytable import PrettyTable
from datetime import datetime

#Import the python file which contain the function.
import Sub.Percolation

#Defining the function called check_idle(.
def check_idle():
    
    if "idlelib.run" in sys.modules:
        return True
    else:
        return False

if check_idle():
    print("This script should be run in the command prompt, not in Python IDLE.")
    sys.exit(1)


#Use error handling.
try:
    #Calling the function.
    Sub.Percolation.percolation_Function()

except Exception as e:
    print("An error occured:",e)
    sys.exit("Existing due to error.")
    
