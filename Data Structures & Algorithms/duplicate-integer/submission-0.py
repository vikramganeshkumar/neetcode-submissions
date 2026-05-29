class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we can store using a hash set and check if the hash set valie is equal to the original list.
        #time complexity is O(n)
        #space complexity O(n)
        hashset = set()
        for num in nums:
            if num in hashset:
                return True 
            else:
                hashset.add(num)#adding the num in the hashset
        return False
        