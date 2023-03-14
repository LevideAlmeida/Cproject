def add_client(name, list=[]):
    list.append(name)
    return list

client1 = add_client('Vitoria')
add_client('Emily', client1)
print(client1)

client2 = add_client('Policarpo')
add_client('Luzia', client2)
print(client2)

# Client1 and client2 are pointing to the same list
# Why?
'''
def add_client(name, list=[])
    when we use a list as keyword argument, when we execute the function
    without passing argument, the interpreter uses the previously created
    list like a argument.

    Ex:
    client1 = add_client('Vitoria')
    # add_client return a list

    add_client('Emily', client1)
    # 'Emily' is append in client1

    client2 = add_client('Policarpo')
    # No list passed, then interpreter will use the client1 as argument
'''
# Ok. Now, how to solve it?
# Simple, Not use mutable with parameters in a function.

def add_client(name, list=None):
    # Now for have a list in case the user doesn't pass it, use an if.
    if list is None:
        list=[]
    list.append(name)
    return list

client1 = add_client('Vitoria')
add_client('Emily', client1)
print(client1)

client2 = add_client('Policarpo')
add_client('Luzia', client2)
print(client2)

# Now, client1 and client2 are pointing to different lists
