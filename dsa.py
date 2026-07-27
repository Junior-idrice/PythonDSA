# working on dsa and this is a great course
'''
def locate_value(cards, query):
    position = 0
    while True:

        if cards[position] == query:
            return position
        position += 1 
        if position == len(cards):
            return -1
test = {
    'input':{
        'cards': [7,9,6,5,8,1,0],
        'query':8
    },
    'output':4
}

result = locate_value(*test['input'].values())
print(result)
print(result ==  test['output'])'''

#Binary search\
def test_location(cards, query,mid):
    mid_number  = cards[mid]

    if mid_number == query:
        if mid-1>0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'right'
    else:
        return 'left'

def locate_card(elements,query):
    start = 0
    end = len(elements)-1

    while start <= end:
        mid = (start + end)//2
        mid_num = elements[mid]
        print("start: "+ str(start) + " end: "+ str(end)+ " middle val: "+ str(mid_num)+ " mid "+ str(mid))
        results = test_location(elements, query, mid)
        if results == 'found':
            return  mid
        elif results == 'left':
            end = mid-1
        elif results == 'right': 
            start = mid + 1
    return -1


elt = [4,5,6,8,8,9,10,16,17,19,23,100]
print(locate_card(elt, 23))


        