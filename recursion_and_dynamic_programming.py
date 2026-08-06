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
    if idx1 == len(seq1) and idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1,seq2, idx1+1, idx2+1)
    else:
        option1 = lcs_recursive(seq1,seq2, idx1+1, idx2)
        option2  = lcs_recursive(seq1, seq2, idx1, idx2+1)
        return max(option1, option2)









