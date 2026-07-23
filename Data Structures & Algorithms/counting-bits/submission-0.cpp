class Solution {
public:
    vector<int> countBits(int n) {
         vector<int> dp(n+1,0);
         int j=0;
        while(j<=n){
            
            
            dp[j] = dp[j >> 1] + (j & 1);
            j++;
        }
        return dp;
    }
};
