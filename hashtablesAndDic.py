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

MAX_HASH_TABLE_SIZE  = 4096


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
basic_table.insert("silent", "19")
basic_table.insert("listen", "20")

print(basic_table.list_all())
print("-"*28)
##print(len(basic_table.data_list) == 1024)
#basic_table.update("idrice", 10)

#print(basic_table.find("idrice"))

#Now the big part of this is when we have hashtable collisions, where 2 or more values have the same hash,
# For example Silent and Listen
# if we call get_index on both we get 655
# So how does that works now
# We can use buckets or linear probing to solve this
# But we will use Linear probing to go about it here

# We create a function for this

def get_valid_index(data_list, key):
    idx = get_index(data_list, key)
    start_idx = idx
    while True:
        kv = data_list[idx]

        if kv is None:
            return idx
        k, v = kv
        if k == key:
            return idx
        idx = (idx + 1) % len(data_list)
        if idx == start_idx:
            raise Exception("Hash table is full")
        '''idx +=1 
        if idx == len(data_list):
            idx = 0'''

data  = [None] * 1024
data[get_valid_index(data, "listen")] = "listen", "first"
print(get_valid_index(data, "listen"))
print(get_valid_index(data, "silent"))


# Let do a hash table for the linear probing

class ProbingHashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data_list = [None]* max_size
    def insert(self,key, value):
        idx  = get_valid_index(self.data_list, key)

        self.data_list[idx] = (key,value)

    def find(self,key):
        idx = get_valid_index(self.data_list, key)

        kv = data_list[idx]
        return None if kv is None else kv[1]
    def update(self,key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = (key, value)
    def list_all(self):
        return [kv for kv in self.data_list if kv is not None]


probingtable = ProbingHashTable(max_size=1024)
probingtable.insert("listen", "19")
probingtable.insert("silent", "20")

print(probingtable.list_all())

"AND THIS IS ALL ABOUT HASHING AND ALL THAT WORKS WITH IT"
# very good code 











