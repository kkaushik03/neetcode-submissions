class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]
        for num in nums:
            heapq.heappush(pq,-num)
        for i in range(1,k+1):
            result = - heapq.heappop(pq)
        return result