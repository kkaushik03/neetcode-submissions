class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq=[]
        result = []
        for x1,y1 in points:
            pushed=x1**2 + y1**2
            pushed = pushed**0.5
            heapq.heappush(pq,(pushed,[x1,y1]))
        for i in range (1,k+1):
            twin1,twin2=heapq.heappop(pq)
            result.append(twin2)
        return result
