# to open the file, use:
# with open('file name', 'opening mode') as file_alias:
# using just file name, the file will be created in the main module.
# To create file in a specific directory, use the path.

# Opening modes:
# 'x' => Create file.
# 'w' => Write.
# 'r' => Read.
# 'w+' => Write plus Read.
# 'r+' => Read plus Write.
# 'b' => Binare.
# 'a' => Write.

# 'w' and 'a' diference:
# 'w': Erase the file and write.
# 'a': Write to end of file without erase.

file_name = 'File.txt'

with open(file_name, 'a') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
    file.write('Line 4\n')

with open(file_name, 'r') as file:
    text_file = file.read()
    file.seek(0,0)
    print(file.read())

with open(file_name, 'w') as file:
    file.write(text_file)
