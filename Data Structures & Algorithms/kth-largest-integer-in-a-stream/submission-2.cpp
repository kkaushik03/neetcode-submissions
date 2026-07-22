class KthLargest {
public:
    priority_queue<int  , vector<int>, greater<int>> pq;  // min-heap
    int k_; 
    KthLargest(int k, vector<int>& nums) {
    k_=k;
    for(int num:nums)
        add(num);
    }

    int add(int val) {
        pq.push(val);
        if(pq.size()>k_)
            pq.pop();  // keep only the k largest
        return pq.top();
    }
};
