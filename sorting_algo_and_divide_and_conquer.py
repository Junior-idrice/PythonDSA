'''
Question:
you're working on a new feature on Idrice's "TOP NOTEBOOLS OF THE WEEK
". Write a function to sort a list of notebooks in decreasing order of likes.
Kepp in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible


'''

#simple form to sort element in a list

def sort(nums):
    pass
#list of numbers in random order
test0 = {
    'input':{
        'nums': [4,2,6,3,4,6,2,1]
    },
    'output':[1,2,2,3,4,4,6,6]
}
#list of numbers in random order
test1 = {
    'input':{
        'nums': [5,2,6,1,25,7,-12,12,-243,0]
     },
        'output':[-243,-12,0,2,5,6,7,12,23]
}
#list is already sorted
test2 = {
    'input':{
        'nums': [3,5,6,8,9,10,99]
     },
        'output':[3,5,6,8,9,10,99]
}
#list sorted in descending order
test3 = {
    'input':{
        'nums': [99,10,9,8,6,5,3]
     },
        'output':[3,5,6,8,9,10,99]
}
#list containing repeating elements
test4 = {
    'input':{
        'nums': [5,-12,2,6,1,23,7,8,-12,6,12,1,-243,1,0]
     },
        'output':[-243,-12,-12,0,1,1,1,2,5,6,6,7,7,12,23]
}
#empty list
test5 = {
    'input':{
        'nums': []
     },
        'output':[]
}
#list containing just one element
test6 = {
    'input':{
        'nums': [23]
     },
        'output':[23]
}
#list containing one repeated element
test6 = {
    'input':{
        'nums': [42,42,42,42,42,42,42,42]
     },
        'output':[42,42,42,42,42,42,42,42]
}



import random 
in_list= list(range(10000))
out_list = list(range(1000))
random.shuffle(in_list)

test8 = {
    'input': { 
        'nums':in_list},
    'output': out_list
}


# Bubble sort
def bubble_sort(nums):
    num = list(nums)

    #iterate over the array
    for _ in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i]> nums[i+1]:
                nums[i], nums[i+1]= nums[i+1], nums[i]
    return nums
a  = [3,3,3,3]

print(bubble_sort(a))