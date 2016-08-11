# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
#imports
import copy

#body
def is_sorted(any_list):
    new_list = copy.deepcopy(any_list)
    any_list.sort()
    if new_list == any_list:
        return True
    else:
        return False

##################################################################
def main():

    pass
    
if __name__ == '__main__':
    main()