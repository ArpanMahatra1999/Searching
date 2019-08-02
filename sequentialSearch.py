def sequentialSearch(A,k):
    i = 0
    while(A[i]!=k):
        i = i+1
    if i<len(A):
        return i
    else:
        return -1

A = [9,8,4,3,4,3,6,2,8,9]

print(A)
print("The value is present at position ",sequentialSearch(A,2)+1,".")