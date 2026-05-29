class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):#i is the value not the key
            difference = target - nums[i]#its the key
            if difference in hashmap: ## asking "is diff one of the keys?"
                return [hashmap[difference], i]
            hashmap[nums[i]] = i#assinging index value
        
        