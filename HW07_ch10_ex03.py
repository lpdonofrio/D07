# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

#imports

#body
def cumulative_sum(any_list):
    new_list = []
    new_list.append(any_list[0])
    first = 1
    second = 0
    while len(new_list) < len(any_list):
        new_list.append((any_list[first] + new_list[second]))
        first += 1
        second += 1
    return new_list


##################################################################
def main():

    pass
    
if __name__ == '__main__':
    main()