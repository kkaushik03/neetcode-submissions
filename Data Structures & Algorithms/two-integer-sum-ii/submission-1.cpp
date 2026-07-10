class Solution {
public:
   vector<int> twoSum(vector<int>& numbers, int target) {
    unordered_map<int, int> seen;   // number -> index
    for (int i = 0; i < numbers.size(); i++) {
        int complement = target - numbers[i];
        if (seen.find(complement) != seen.end()) {
            return {seen[complement] + 1, i + 1};   // <-- both need +1
        }
        seen[numbers[i]] = i;
    }
    return {};
}
};
