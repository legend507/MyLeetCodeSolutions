# 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for a_char in ransomNote:
            if a_char not in magazine:
                return False
            
            # Remove the used a_char from magazine.
            pos = magazine.find(a_char)
            magazine = magazine[:pos] + magazine[pos+1:]
        
        return True