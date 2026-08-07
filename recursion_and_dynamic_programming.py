## Longest Common Subsequence
'''
Question1:
write a function to find the length of the longest common subsequence between
two sequences. E.g Given the strings "serendipitous" and "precipitation", the 
longest common subsequence is "reipito" and its length is 7

A "sequence" is a group of items with a deterministic ordering. List,tuples and
ranges are some common sequence types in python

A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence.
For example, "edpt" is a subsequence of "serendipitous"
#great question
'''



'''
Test Cases
General case (string)
General case (list)
no common subsequence
one is a subsequence of the other
one sequence is empty
both sequence are empty

'''
t0 = {
    'input':{
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}
t1 = {
    'input':{
        'seq1': [1,3,5,6,7,2,5,2,3],
        'seq2': [6,2,4,7,1,5,6,2,3]
    },
    'output': 5
}
t2 = {
    'input':{
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}
t3 = {
    'input':{
        'seq1': 'asdfwevad',
        'seq2': 'opkopiklj'
    },
    'output': 0
}
t4 = {
    'input':{
        'seq1': 'dense',
        'seq2':'condensed'
    },
    'output': 5
}
t5 = {
    'input':{
        'seq1': '',
        'seq2': 'popklklk'
    },
    'output': 0
}

t6 = {
    'input':{
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}
t7 = {
    'input':{
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}

lcs_tests = [t0,t1,t2,t3,t4,t5,t6,t7] 

def lcs_recursive(seq1,seq2,idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1,seq2, idx1+1, idx2+1)
    else:
        option1 = lcs_recursive(seq1,seq2, idx1+1, idx2)
        option2  = lcs_recursive(seq1, seq2, idx1, idx2+1)
        return max(option1, option2)

#print(lcs_recursive(**t5['input']))
'''for test in lcs_tests:
    print(lcs_recursive(**test['input']))
    print(test['output'])
    print("-----------------------")'''
 
# There is a lot of inefficiency because there my be some repetitions that occur
# Let's get the complexity
# let suppose the string are of length m and n, the we have m+n choices to make
# since we divide my two, we then have O(2^(m+n)) leafs to complete this operation
# this is very bad 
# Space = O(m+n)


## Let's try to improve this solution because it takes soo much time 
# to improve this, we have to keep track of operations that have already been 
# performed so as to not go back to them and consume time for nothing
# we called this MEMOIZATION and we use a dictionary to keep track of 
# all these

def lcs_memo(seq1,seq2):
    memo = {}
    def recurse(idx1=0, idx2=0):
        key = (idx1,idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
        return memo[key]
    return recurse(0,0)

for test in lcs_tests:
    print(lcs_memo(**test['input']))
    print(test['output'])
    print("-----------------------")

## Here the complexity is O(m*n) which is very efficient and great

# Memoization is good but has recursive calls which can be an overhead
# We will use dynamic programming to go about this (iteration)
#  how does dynamic programming help to the longest common subsequence

#I see they say, create a table of size
#1 - (n1+1)*(n2+1) initialized with 0s, where n1 and n2 are the length of
 #the sequences. table[i][j] represents the lcs of seq1[:i] and seq2[:j]

#2- if seq1[i] and seq2[j] are equal, then table[i+1][j+1]=1 + table[i][j]
#3 - if seq1[i] and seq2[j] are equal, then table[i+1][j+1]=max(table[i][j+1],table[i+1][j])
#  Here the timecomplexity is O(N1*N2) which is creating the table, equally the space complexity

def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i+1][j+1] = 1 + table[i][j]
            else:
                table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
    return table[-1][-1]

for test in lcs_tests:
    print(lcs_dp(**test['input']))
    print(test['output'])
    print("-----------------------")
