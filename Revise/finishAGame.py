# https://brainly.com/question/48293913
nums = [7, 4, 9, 10]

x = 4
count = 1 
l, r = 0, 1
currMin = currMax = nums[l] 
while r < len(nums):
    currMax = max(currMax, nums[r]) 
    currMin = min(currMin, nums[r])
    # print("currMax:", currMax)
    # print("currMin:", currMin)
    
    if nums[r] > nums[l]: 
        gap = nums[r] - currMin
    elif nums[l] >= nums[r]:
        gap = currMax - nums[r]
        
    # print("gap:", gap)
            
    if gap > x:
        count += 1
        currMin = currMax = nums[l + 1] 
        
    # print("count:", count)
    l += 1 
    r += 1
   
print(count) 