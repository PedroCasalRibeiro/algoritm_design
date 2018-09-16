
# coding: utf-8

# In[ ]:


listOfTuples = []
n = int(input())
for i in range(n):
    beg, end = map(int, input().split())
    listOfTuples.append((beg, end))

sortedBeg = sorted(listOfTuples, key=lambda x: x[0])
sortedEnd = sorted(listOfTuples, key=lambda x: x[1])

thrhold = sortedBeg[0][0] - 1
listOfPoints = []
for i in range(len(sortedEnd)-1):
    beg, end = sortedEnd[i]
    if beg > thrhold:
        listOfPoints.append(end)
        thrhold = end

if listOfPoints[len(listOfPoints) - 1] < sortedEnd[len(sortedEnd) - 1][0]:
    if sortedEnd:
        listOfPoints.append(sortedEnd[len(sortedEnd) - 1][0])
print(len(listOfPoints))
result = []
for p in listOfPoints:
    result.append(p)

print(*result)


# In[ ]:


n = int(input())

total = 0
increment = 1
count = 0
listOfNum = []

while total + increment <= n:
    total += increment
    listOfNum.append(increment)
    increment += 1
    count += 1

listOfNum[count-1] += n - total

print(count)
print(*listOfNum)


# In[ ]:


def filler(token):
    while len(token) < 3:
        token += token[-1]
    return token


def solution(tokens):
    tokens.sort(key=filler, reverse=True)

    return ''.join(tokens)


if __name__ == '__main__':
    input()  # skip header
    data = list(input().split())

    print(solution(data))


# In[ ]:


a = [0]*100
for i in range (100):
    a[i] = i
print (a)
k = 88
a[99] = 88
for i in range(len(a)):
    if a[i] == k:
        print ('yes!')
        break
    print (i,  'no!')


# In[11]:


def binarysearch (A, low, high, key):
    if high >= low:
        mid = int(low + ((high-low))/2)
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binarysearch(A, low, mid-1, key)
        elif key > A[mid]:
            return binarysearch (A, mid+1, high, key)
    else:
        return -1
    
def Binarysearch (A, low, high, key):
    while low <= high:
        mid = int(low + ((high-low))/2)
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid-1
        elif key > A[mid]:
            low = mid +1
    return -1


# In[6]:


import random
A = [0]*100000

for x in range(len(A)):
  A[x] = random.randint(1,100001)


# In[7]:


A.sort()


# In[13]:


result = binarysearch(A, 0, len(A)-1, 35000)
if result != -1: 
    print ("Element is present at index %d" % result) 
else: 
    print ("Element is not present in array")


# In[20]:


B = []
with open('4_1_binary_search.in') as f:
    input = f.read()
    data = list(map(int, input.split()))
    n = data[0]#integer for the length of the array
    m = data[n + 1]#last entry in the sorted array
    a = data[1 : n + 1]#all entries in the sorted array
for x in data[n + 2:]:#starts iterating the unsorted search terms as x
    binarysearch(a,x,0,n)
    B.append(1)
print (len(B))

