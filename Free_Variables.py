# Free variables (locals, globals) + nonlocal
# print(*globals(), sep='\n')
# print(*locals(), sep='\n')

def concatenate(string):
    final_value = string #final_value is a free variable
    def internal_function(concatenate_value):
        return final_value + concatenate_value

        """
        # final_value += concatenate_value
        # return final_value
        this code generate an error, because final_value is a free variable
        so final_values cannot be changed in the internal funcition, but with nonlocal this is possible
        """
    return internal_function

concatenation = concatenate('a')
print(concatenation('b'))

# Function with nonlocal
def concatenate(string):
    final_value = string
    def internal_function(concatenate_value):
        nonlocal final_value # now final_value can be changed in internal
        final_value += concatenate_value
        return final_value
    return internal_function

concatenation = concatenate('a')
print(concatenation('b'))
print(concatenation('c'))
print(concatenation('d'))
# now final_value have your value be changed every time that concatenate function is executed
