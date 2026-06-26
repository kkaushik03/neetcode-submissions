class MinStack {
    private:
        stack<pair<int,int>> minstack_;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        int currentMin = minstack_.empty() ? val : min(minstack_.top().second, val);
        minstack_.push({val, currentMin});
    }
    
    void pop() {
        minstack_.pop();
    }
    
    int top() {
        return minstack_.top().first;
    }
    
    int getMin() {
        return minstack_.top().second;
    }
};
