import os

file_to_save = os.path.join("C:/python", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
     txt_file.write("Arapahoe\n")
     txt_file.write("Denver\n")
     txt_file.write("Jefferson")
