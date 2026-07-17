class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        array<int, 26> need{}, window{};
        for(char c : s1){
            need[c-'a']++;
        }
        //we have the need array now; 
        for(int i = 0;  i + s1.length() <= s2.length(); i++){
             window.fill(0);
             for(int j = i; j < s1.length()+i; j++){
                window[s2.at(j)-'a']++;
             }
             if(window==need)
                return true; 
        }
        return false;
    }
};