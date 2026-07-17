class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> store;

    TimeMap() {
    }
    void set(string key, string value, int timestamp) {
     //for set:
    store[key].push_back({timestamp, value});
           
    }
    
    string get(string key, int timestamp) {
         if (store.find(key) == store.end()) return "";
        auto& v = store[key];

        int lo = 0, hi = v.size() - 1;
        string ans = "";                    // stays "" if nothing qualifies
        while (lo <= hi) {                  // mid recomputed EVERY iteration
            int mid = lo + (hi - lo) / 2;
            if (v[mid].first <= timestamp) {
                ans = v[mid].second;        // bank the candidate
                lo = mid + 1;               // a larger valid timestamp can only be to the right
            } else {
                hi = mid - 1;               // mid is too new; so is everything right of it
            }
        }
        return ans;


    }
};
