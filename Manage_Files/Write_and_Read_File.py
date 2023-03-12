separator = '-' * 86

file_name = 'File.txt'

with open(file_name, 'w+') as file: # 'w+' => Write plus Read
    file.write('I am Python\n')
    file.write('The true python is the friends that we make along the way\n')

    print(file.read()) # Nothing happens
    file.seek(0,0) # Moving python cursor to the begin
    print(file.read()) # Read
    print(separator)

    file.writelines(
        ('line 3\n', 'line 4\n')
    )   # Writing multiple lines

    file.seek(0,0)
    print(file.read())
    print(separator)

    file.seek(0,0)
    print(file.readline(), end='') # Reading the line where cursor is
    print(file.readline(), end='') # next
    print(file.readline().strip()) # next
    print(file.readline().strip()) # next
    print(separator)

    # readlines => returns iterable with all lines
    print('READLINES')
    file.seek(0,0)
    for line in file.readlines():
        print(line, end='')

    file.seek(0,0)
