class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> total_sum; 
        vector<int> result; 
        int count = 1; 
        for(int number: numbers){
            int second = target-number; 
            if(total_sum.find(second)==total_sum.end()){ 
                total_sum[number]=count;
            }
            else //complement
            {
                int first =total_sum[target-number];
                result.push_back(first);
                result.push_back(count);
                return result; 
            }
            count ++;
        }
        return result; 
    }
};
