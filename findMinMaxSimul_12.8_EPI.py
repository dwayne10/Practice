def findMinMaxSim(nums):
    def compare(num1, num2):
        return [num1, num2] if num1 < num2 else [num2,num1]

    min_max_so_far  = compare(nums[0], nums[1])
    for i in range(2, len(nums) - 1):
        local_min_max = compare(nums[i], nums[i+1]) # done to save one
        # comparision
        min_max_so_far = [min( min_max_so_far[0], local_min_max[0]),
                          max(min_max_so_far[1], local_min_max[1])]
    return  min_max_so_far

print(findMinMaxSim([3,0,0,-1,10,6,15]))