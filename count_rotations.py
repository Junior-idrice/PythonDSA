# this function takes a rotated list and tries to know the number
# of times the list was rotated and so on

# THIS TRICK
'''------if a list of sorted elements is rotated k times then the smallest
 number in the list ends up at position k--------'''


test1 = {
    'input':{
        'nums': [19,25,29,3,5,6,7,9,11,14]
    },
    'output': 3  
}
test2 = {
    'input':{
        'nums': [1,2,3,4,5,6]
    },
    'output': 0
}
test3 = {
    'input':{
        'nums': [5,1,2,3,4]
    },
    'output': 1
}
test4 = {
    'input':{
        'nums': [2,3,4,5,6,7,1]
    },
    'output': 6
}
test5 = {
    'input':{
        'nums': [1,2,3,4,5,6]
    },
    'output': 0
}
test6 = {
    'input':{
        'nums': [5]
    },
    'output': 0
}

#USING LINEAR SEARCH
#  here we simple check every element with the predecesoor, then we found the disorder and that's all


def count_rotations(nums):
    position = 0
    while position < len(nums):
        if position>= 0 and nums[position-1] > nums[position]:
            return position
        position +=1
    return 0

# Using binary search: we check for the middle element and compare it to the predecossor. if he is bigger, then we are done
# other wise, since we are looking for the smallest number we simply compare. since we know that the list is sorted, we compare the middle element and the 
# the last element. if the middle is bigger than the last element, then the smallest is in that range
# if the middle is smaller than the last, then the smallest lies between the start and the middle 


def binary_rotation_count(nums):
    lo = 0
    hi = len(nums)-1
    
    while lo<hi:
        mid = (lo+hi)//2
        if mid>=0 and nums[mid-1]> nums[mid]:
            return mid
        elif nums[mid] < nums[hi]:
            hi = mid-1
        elif nums[mid]> nums[hi]:
            lo = mid +1 
    return 0





test_all = [test1,test2,test3,test4,test5,test6]
i = 1
for test in test_all:
    print("test: "+ str(i))
    nums0 = test['input']['nums']
    print(nums0)
    output0 = test['output']
    print(output0)


    # this is for linear search result0 = count_rotations(nums0)
    #print(result0)
    result0 = binary_rotation_count(nums0)
    print('*'*20)
    i += 1
