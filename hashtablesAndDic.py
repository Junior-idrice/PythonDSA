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
print(elts)