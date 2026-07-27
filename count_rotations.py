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
        'nums': [1,2,3,4,5]
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

#USING LINEAR SEARHC

def count_rotations(nums):
    position = 0
    while position < len(nums):
        if position>= 0 and nums[position-1] > nums[position]:
            return position
        position +=1
    return 0
    


test_all = [test1,test2,test3,test4,test5,test6]
for test in test_all:
    nums0 = test['input']['nums']
    print(nums0)
    output0 = test['output']
    print(output0)

    result0 = count_rotations(nums0)
    print(result0)
    print('*'*20)


'''
nums0 = test6['input']['nums']
print(nums0)

output0 = test6['output']
print(output0)

result0 = count_rotations(nums0)
print(result0)'''