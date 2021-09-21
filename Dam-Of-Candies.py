class Solution:
    def maxCandy(self, h, n): 
        # Your code goes here
        area=0
        i=0
        j=n-1
        
        while(i<j): 
            
            if(h[i]<h[j]):
                area=max(area, (j-i-1)*h[i])
                i+=1
            elif h[i]>h[j]:
                area=max(area, (j-i-1)*(h[j]))
                j-=1
            else:
                area=max(area, (j-i-1)*h[i])
                i+=1
                j-=1
                
        
        return area

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.maxCandy(arr,n))