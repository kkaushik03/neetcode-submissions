class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res=-1;
        for(int num:nums){
            res = res^num;
        }
        int j = 0; 
        while(j<=nums.size()){
            res=res^j; 
            j++; 
        }
        return res^-1; 
    }
};
