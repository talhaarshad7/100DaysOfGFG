class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
        total_len=len(array1) + len(array2)
        array1.extend(array2)
        array1.sort()
        if total_len%2!=0:
            return (array1[total_len//2])
        else:
            mid=total_len//2
            avg=array1[mid] + array1[mid-1]
            if avg%2==0:
                return avg//2
            else:
                return avg/2

if __name__ == "__main__":
    t=int(input())

    for _ in range(t):
        m=input()
        arr1=[int(x) for x in input().split()]
        n=input()
        arr2=[int(x) for x in input().split()]

        ob=Solution()
        print(ob.MedianOfArrays(arr1,arr2))