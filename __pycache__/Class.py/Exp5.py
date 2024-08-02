# Write an experiment to swap two coloumns in numpy array.

import numpy as np 
 
# Create a numpy array 
arr = np.array([[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]]) 
print("Original Array:") 
print(arr) 
 
# Asking the user for column indices to swap
try: 
 column1_index = int(input("Enter the index of the first column to swap: "))    
 column2_index = int(input("Enter the index of the second column to swap: ")) 

# Check if the provided indices are within the valid range 
 if column1_index < 0 or column1_index >= arr.shape[1] or column2_index < 0 or column2_index >= arr.shape[1]:        
    print("Invalid column indices. Please provide valid indices.")    
 else: 
        # Swap the specified columns 
        arr[:,[column1_index, column2_index]] = arr[:,[column2_index, column1_index]] 
         
        # Print the array after swapping         
        print("Array after swapping columns:")         
 print(arr) 
except ValueError: 
 print("Invalid input. Please enter valid integers for column indices.") 

