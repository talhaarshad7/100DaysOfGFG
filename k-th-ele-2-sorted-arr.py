class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        arr1.extend(arr2)
        arr1.sort()
        #print(arr1)
        return arr1[k-1]

def main():
    t=int(input())

    while(t!=0):
        n,m,k=[int(x) for x in input().split()]
        a=[int(x) for x in input().split()]
        b=[int(x) for x in input().split()]

        ob=Solution()
        print(ob.kthElement(a,b,n,m,k))

        t-=1

if __name__ == "__main__":
    main()