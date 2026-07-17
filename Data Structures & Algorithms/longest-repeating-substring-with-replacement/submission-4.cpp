class Solution {
public:
    int characterReplacement(string s, int k) {
        int left=0; 
        int right=0;
        int maxlen=0;
        unordered_map<char,int> wordle; 
        for(char c:s){
            right++;    
            if(wordle.find(c)==wordle.end())
                wordle[c]=1; 
            else
                wordle[c]++;
            maxlen=max(maxlen,wordle[c]);
            if((right-left)-maxlen>k)
            {
                wordle[s[left]]--;
                if(wordle[s[left]]==0)
                    wordle.erase(s[left]);
                left++;
            }

        }
        return right-left; 
    }
};
