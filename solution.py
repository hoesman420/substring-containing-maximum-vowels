class Solution:
    def maxVowels(self, s: str, k: int) -> str:
        vowels = set("aeiou")
        ans = cnt = sum(c in vowels for c in s[:k])
        max_start_index = 0 
        
        for i in range(k, len(s)):
            cnt += int(s[i] in vowels) - int(s[i - k] in vowels)
            if cnt > ans:
                ans = cnt
                max_start_index = i - k + 1  
        
       
        return s[max_start_index:max_start_index + k]

# Example usage:
sol = Solution()
result = sol.maxVowels("aeiouia", 5)
print(result)
