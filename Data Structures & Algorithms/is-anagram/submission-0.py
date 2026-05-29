class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Space complexity is O(n) or 0(1) if char in hashmap doesnt exceed 26 
        #Time Complexity is O(n)
        #store the strings in hasmap and compare if they are equal
        s1 = {}
        for char in s:
            if char in s1:#checking if char alr exists in the hashmap
                s1[char] += 1
            else:
                s1[char] = 1
        s2 = {}
        for char in t:
            if char in s2:
                s2[char] += 1
            else:
                s2[char] = 1
        return s1 == s2
        