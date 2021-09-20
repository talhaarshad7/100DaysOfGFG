class Solution:
    def factorial(self, N):
        #code here
        m=1
        if N==0:
            return str(1)
        else:
            while(N>=1):             #Integers in Python 3 are limited only by available memory.
                m=m*N
                N=N-1
            return str(m)

if __name__ == "__main__":
    t=int(input())

    for _ in range(t):
        N=int(input())
        ob=Solution()
        ans=ob.factorial(N)
        for i in ans:
            print(i,end="")
        print()