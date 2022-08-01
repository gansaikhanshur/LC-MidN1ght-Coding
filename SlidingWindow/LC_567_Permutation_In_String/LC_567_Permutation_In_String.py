class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter, s2_counter = collections.Counter(s1), collections.defaultdict(int)
        window_length = len(s1)
        
        l = 0
        for idx, val in enumerate(s2):
            
            s2_counter[s2[idx]] += 1
            if (idx - l + 1) == window_length:
                if s1_counter == s2_counter:
                    return True
                
                if s2_counter[s2[l]] == 1:
                    del s2_counter[s2[l]]
                else:
                    s2_counter[s2[l]] -= 1
                l += 1
            
        return False
            
            
        
