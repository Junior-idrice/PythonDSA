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
'''

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
    i += 1'''


# ------------------ ANOTHER BIG QUESTIONS -------------------------------# 


# given a rotated array, how do you find for a number
# first, we can simple the array in the two sections 

def find(values):
    low = 0
    high = len(values)-1

    while low <= high:
        mid = (low+high)//2

        if values[mid-1] > values[mid] :
            return mid
        elif values[mid] < values[high]:
            high = mid - 1
        elif values[mid] > values[high]:
            low = mid + 1
    return 0

def apply_binary(values,query):
    result = find(values)
    first_low, first_high= 0, result-1
    second_low, second_high = result, len(values)-1

    if values[first_low]<=query<=values[first_high]:
        
        while first_low <= first_high:
            middle = (first_high+first_low)//2
            if values[middle] == query:
                return middle
            elif values[middle]< query:
                first_low = middle + 1
            else:
                first_high = middle - 1

    elif values[second_low]<= query<= values[second_high]:
        
        while second_low <= second_high:
            middle = (second_low+second_high)//2
            if values[middle] == query:
                return middle
            elif values[middle]< query:
                second_low = middle + 1 
            else:
                second_high = middle - 1

    return -1

print(apply_binary([2,1], 1))          # 1
print(apply_binary([2,1], 2))          # 0

print(apply_binary([1,2], 1))          # 0
print(apply_binary([1,2], 2))          # 1

print(apply_binary([5,6,1,2,3,4], 4))  # 5
print(apply_binary([5,6,1,2,3,4], 6))  # 1
print(apply_binary([5,6,1,2,3,4], 5))  # 0
print(apply_binary([5,6,1,2,3,4], 7))  # -1

print(apply_binary([1], 1))            # 0
print(apply_binary([1], 2))            # -1