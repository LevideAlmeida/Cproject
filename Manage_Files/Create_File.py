# Create files
# Use the function open()
# To create a file is necessary the path

file_path = '/home/luan/workspace/PythonProject/Manage_Files/'
file_path += 'Create_File.txt' # File name
# Full path = /home/luan/workspace/PythonProject/Manage_Files/Create,File.txt
#

# file = open(file_path, 'w')
# file.close() # Never forget, CLOSE file before running the code

# Context manager - with (open and close file)
with open(file_path, 'w') as file:
    print('hello world')
