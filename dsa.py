# working on dsa and this is a great course

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
print(result ==  test['output'])
        