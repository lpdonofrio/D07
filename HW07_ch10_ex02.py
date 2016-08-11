# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

#imports

#body
def capitalize_nested(any_list):
    capitalized_list = []
    for item in any_list:
        if type(item) == list:
            capitalized_list.append(capitalize_nested(item))
        else:
            capitalized_list.append(item.capitalize())
    return capitalized_list


x = ['apple', ['bear', ['hi']], 'cat']
capitalize_nested(x)

##################################################################
def main():

    pass
    
if __name__ == '__main__':
    main()