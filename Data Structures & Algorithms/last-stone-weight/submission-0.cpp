
class Solution {
   public:
    priority_queue<int, vector<int>> pq;
    int lastStoneWeight(vector<int>& stones) {
        for (int element : stones) {
            pq.push(element);
        }
        while (pq.size() >= 2) {
            int element1 = pq.top();
            pq.pop();
            int element2 = pq.top();
            pq.pop();
            if (element1 == element2) {
            } else
                pq.push(abs(element1 - element2));
        }
       return pq.empty() ? 0 : pq.top();
    }
};
