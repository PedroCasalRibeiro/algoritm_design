
# coding: utf-8

# In[3]:


# Currency and change
money = [1, 5, 10]
n = len(money)
 
def findMin(V):
    ans = []
    lib = {}
    count = 0
    i = n-1
    while (i>=0):
        while (V >= money[i]):
           V = V - money[i]
           ans.append(money[i])
        i -= 1
    money.sort(reverse=True)
    for coin in ans:
        for i in range(n-1):
            while coin == money[i]:
                count += 1
                i+= 1
        lib[coin] = count
        count = 0
    return len(ans)
V = 997
findMin(V)

