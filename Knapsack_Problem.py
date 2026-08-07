# DYNAMIC PROGRAMMING
#Knapsack Problem

'''
Problem statement
- You're in charge of selecting a football(soccer) team from 
a large pool of players. Each player has a cost, and a rating
You have a limited budget. What is the highest total rating
of a team that fits within your budget. Assume that there's
no minimum or maximum team size

GENERAL PROBLEM STATEMENT
Given n elements, each of which has a weight and a profit,
determine the maximum profit that can be obtained by selecting
a subset of the elements weighing no more than w

you have the data below
profit       [2,3,1,5,4,7]
weight       [4,5,1,3,2,5]
capacity     15

To exhaust all the 15 capacity, we have to take the combination of weight 
which yield the max profit, and that is weights 5,3,2 and 5

'''

# POSSIBLE TEST CASES ARE
'''
- Some generic test cases
- All the elements can be included
- None of the elements can be included
- Only one of the elements can be included
- You do not use the complete capacity
'''




test0 = {
    'input':{
        'capacity':165,
        'weights':[23,31,29,44,53,38,63,85,89,82],
        'profits':[92,57,49,68,60,43,67,84,87,72]
    },
    'output': 309
}

test1 = {
    'input':{
        'capacity':3,
        'weights':[4,5,6],
        'profits':[1,2,3]
    },
    'output': 0
}
test2 = {
    'input':{
        'capacity':4,
        'weights':[4,5,1],
        'profits':[1,2,3]
    },
    'output': 3
}


def max_profit_recursive(weights, profits,capacity,idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx]> capacity:
        return max_profit_recursive(weights, profits,capacity,idx+1)
    else:
        option1 = max_profit_recursive(weights, profits,capacity,idx+1)
        option2  = profits[idx]+max_profit_recursive(weights,
                                                     profits,
                                                     capacity-weights[idx],idx+1)
        return max(option1, option2)

print(max_profit_recursive(**test0['input']))
print(test0['output'])



