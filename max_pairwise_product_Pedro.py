# Uses python3

user1 = int(input())
a = [int(x) for x in input().split()]
assert (len(a) == user1)
a.sort(reverse=True)
print (a[0]*a[1])
