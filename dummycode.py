# Lab 3 - Ordered list
# Natalie Taylor

# insert an element into a list
def insert(lst, element):
    # sets the index to the length of the list
    index = size
    # loops through the list to find the element placement
    for i in range(size):
        if lst[i] > element:
            index = i
            break
    # if the element needs to be placed at the end of the list
    if index == size:
        # uses concatenation to add the element at the end of the list
        lst = lst[:index] + [element]
    # if the element goes in the beginning or before the end of the list
    else:
        # uses concatenation to add the element in the list.
        # takes the beginning of the list and combines with the element
        # and adds the last bit of the list after the element to insert
        lst = lst[:index] + [element] + lst[index:]
    return lst

# function to print out the whole list separated by spaces on one line
def printlist(list):
    print(*list)

# function to delete an element from the list
def delete(lst, element):
    # sets the index to the length of the list
    index = size
    # loops through list to find the element to remove
    for i in range(size):
        if lst[i] > element:
            index = i
            break
    # if the element is at the end of the list
    if index == size:
        # removes the last element of the list
        lst = lst[:index-1]
    else:
        # concatenates the list from 0 to one before the element
        # with one after the element to be removed --- removed from the list
        lst = lst[:index-1] + lst[index:]
    return lst


list = [2, 3, 6, 9, 10]
size = len(list)
# prints the original list
printlist(list)
# adds the element 1 to the list
newlist = insert(list, 1)
printlist(newlist)
# removes the element 6
printlist(delete(newlist, 6))