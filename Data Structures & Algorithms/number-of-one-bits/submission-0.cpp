class Solution {
public:
    int hammingWeight(uint32_t n) {
        
        int count =0; 
        while(n!=0){
            int offset_n = n-1; 
            n = n & offset_n;
            count++; 
        }
        return count; 
    }
};
