#defining function for array with length of array
def maxElement(arr,n):
    Result = arr[0]
    for i in range(n):
        if arr[i]>Result:
            Result = arr[i]
    return Result

#defining array
arr = [0,2,0,5,9,2,1,6]

#defining n as length of array
n = len(arr)

#printing maximum element
print("The maximum element is ", maxElement(arr,n))