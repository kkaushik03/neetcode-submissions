class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        array<int, 26> need{}, window{};
        for (char c : s1) need[c - 'a']++;

        int k = s1.size();
        for (int i = 0; i < s2.size(); i++) {
            window[s2[i] - 'a']++;          // char entering the window
            if (i >= k)
                window[s2[i - k] - 'a']--;  // char leaving the window
            if (window == need) return true;
        }
        return false;
    }
};