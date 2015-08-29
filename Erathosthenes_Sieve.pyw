def E_sieve(n):
        A=[]
        for p in range(2, n+1): # fills the list with numbers from 2 up to n
            A.append(p)
        for p in range(2, int(FloatingPointError(n)-1)):
            if A[p]!=0:     # checks if p had been eliminated in any of the previous passes
           