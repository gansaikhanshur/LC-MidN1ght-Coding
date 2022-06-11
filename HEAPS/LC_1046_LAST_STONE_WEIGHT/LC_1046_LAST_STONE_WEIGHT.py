class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for idx, val in enumerate(stones):
            stones[idx] = -val
            
        heapify(stones)
        
        while stones:
            stone_a = -heappop(stones)
            if not stones:
                return stone_a
            
            stone_b = -heappop(stones)
            
            if stone_a > stone_b:
                heappush(stones, stone_b - stone_a)
                
        return 0
