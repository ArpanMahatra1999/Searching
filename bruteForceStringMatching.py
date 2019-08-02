def bruteForceStringMatching(T,P):
    n = len(T)
    m = len(P)
    #i runs from 0 to length of T minus length of P as rest isn't required
    for i in range(n-m):
        j = 0
        #while j is less than total character length in P. In "Indu" case, j iterates from 0 to 3 for each position
        while (j<m and P[j]==T[i+j]):
            j=j+1
        #j and m are equal when whole string matching is done till mth position
        if j == m:
            return i
    return -1

T = "Asia's Indus Valley Civilization"
P = "Indu"

print("The string on which matching done:",T)
print("The string to be seeked:",P)
print("The string matches at ",bruteForceStringMatching(T,P)+1)