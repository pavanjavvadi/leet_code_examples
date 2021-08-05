def jump(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        end = 0
        farthest = 0
        jumps = 0
        n = len(nums)
        
        for i in range(0, n):
            
            farthest = max(farthest, i+nums[i])
            
            if i == end and i != n-1:
                jumps += 1
                end = farthest 
        return jumps
            

print(jump([2,3,1,1,4]))