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
'''
def test_location(cards, query,mid):
    mid_number  = cards[mid]

    if mid_number == query:
        if mid-1>=0 and cards[mid-1] == query:
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


elt = list(range(0,10, 1))
print(locate_card(elt, 8))
'''
#BINARY SEARCH

def binary_search(lo,hi, condition):
    while lo<=hi:
        mid = (lo+hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1

    return [-1,-1]

def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid >= 0 and cards[mid-1] == "query":
                return 'left'
            else: return 'found'
        elif cards[mid] < query:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(cards)-1, condition)

elt = list(range(0,10, 1))
print(locate_card(elt, 8))

# Returning the first and last position of an element if it occurs multiple times

def first_position(values, query):
    def condition(mid):
        if values[mid] == query:
            if mid >=0 and values[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif values[mid]< query:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(values)-1, condition)

def last_position(values, query):
    def condition(mid):
        if values[mid] == query:
            if mid < len(values)-1 and values[mid + 1] == query:
                return 'right'
            else:
                return 'found'

        elif values[mid]< query:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(values)-1, condition)

def first_last_position(values,query):
    return first_position(values, query), last_position(values, query)

array = [1,5,12,14,14,15,16]
print(first_last_position(array,0))
