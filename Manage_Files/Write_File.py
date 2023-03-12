
file_name = 'File.txt'

# Opening the file using just it's name, to create the file in the main package
with open(file_name, 'w') as file: # 'w' => Write File
    file.write('Line 1\n')
    file.write('Line 2\n')
