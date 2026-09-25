#Time complexity very high n^3
def sub_arraysum1(array,target):
    n = len(array)
    for i in range(0, n):
        for j in range(i, n+1):
            if sum(array[i:j]) == target:
                return i, j
    return None, None

array = [1,7,4,2,1,3,11,5]
target = 10

#print(sub_arraysum1(array, target))


#optimization
#maintain a running sum for the inner loop
#when the sum exceed the
# Here complexity is n^2
def subarraysum2(array,target):
    n = len(array)
    for i in range(0,n):
        s = 0
        for j in range(i, n+1):
            if s == target:
                return i,j
            elif s> target:
                break
            if j<n:
              s += array[j] 
        
    return None,None
#print(sub_arraysum1(array, target))

#here the time complexity is O(n)
def sub_arraysum3(array,target):
    i,j,s = 0,0,0
    n = len(array)
    while i<n and j<=n:
        if s == target:
            return i, j
        elif s<target:
            if j<n:
                s += array[j]
                j +=1
        elif s> target:
            s -= array[i]
            i += 1
    return None,None
#print(sub_arraysum3([21,1], 22))


#Question 
#Find the minimum number of steps required to convert a string to another string

#these are your input
string1 = "intention"
string2 = "execution"

#output should be a number. In this case 5



"""
test case:
general case 
2. No change required
3. All characters need to be changed
4. string are of equal length
5. unqual length
6. one string is empty
7. the string required just one operations 
"""


"""
Recursion
-if the first character is equal then ignore from both, then solve the rest without the first characters
- what if the characters are not equal like in this example
   - then either that character has to be deleted
      -1  + recursively solve after ignoring the first character of the first string
   -or swapped
       -- 1 + recursively solve after ignoring the first character of each
   - or a character has to be inserted before
         


"""

def min_step(str1, str2,i1=0, i2=0):
    if i1 == len(str1):
        return len(str2) - i2
    elif i2 == len(str2):
        return len(str1)-i1
    elif str1[i1] == str2[i2]:
        return min_step(str1,str2, i1 +1, i2 + 1)
    else:
        return 1 + min(min_step(str1,str2, i1+1, i2), #delete
                       min_step(str1,str2, i1+1, i2+1), #swap
                       min_step(str1,str2, i1, i2+1) # insertion

                       )
    
string1 = 'intention'
string2 = 'execution'  
print(min_step("intention","execution"))