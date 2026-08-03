# Here we will study hash tables
# The ord() function in python converts a character into a number
hashTableHeight= 4096
data_list  = [None] * 3

#print(ord('x'))

def get_index(data_list, a_string):
    result = 0

    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number
    list_index = result % len(data_list)
    return list_index

my_list  = [None]* 48
#print(get_index(my_list, "idrice") )
a = ord("i")+ord("d") + ord("r")+ ord("i") + ord("c")+ ord("e")
#print(a)
#print(a%(len(my_list)))

my_list[get_index(my_list,"idrice")] = ("idrice", 19)
my_list[get_index(my_list, "junior")] = "junior", 20
#print(my_list)

#print(get_index(my_list, "idrice"))

index = get_index(my_list, "idrice")
key, value = my_list[index]
elts = [kv[0] for kv in my_list if kv is not None]
#print(elts)

MAX_HASH_TABLE_SIZE  = 4098


# This is now the big class for it

class BasicHashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def insert(self,key, value):
        idx = get_index(self.data_list, key)

        self.data_list[idx] = (key, value)

    def find(self,key):
        idx = get_index(self.data_list, key)
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    def update(self,key,value):
        idx = get_index(self.data_list, key)
        self.data_list[idx] = (key, value)

    def list_all(self):
        return [kv for kv in self.data_list if kv is not None]

basic_table = BasicHashTable(max_size=1024)

print(len(basic_table.data_list) == 1024)
basic_table.update("idrice", 10)

print(basic_table.find("idrice"))
