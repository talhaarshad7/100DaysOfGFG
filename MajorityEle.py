class Solution:
    def majorityElement(self, A, N):
        #Your code here
        maj=dict()
        for i in A:
            if i not in maj:
                maj[i]=1
            else:
                maj[i]+=1
        #print(maj)
        x=N//2
        flag=0
        for i,j  in maj.items():
            if j>x:
                flag=1
                return i
        if(flag==0):
            return -1
        
import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()