class Solution {
   public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> wordle;
        int count = 0;
        int result = count;
        int left = 0;
        int right = 0;
        for (char c : s) {
            if (wordle.find(c) == wordle.end()) {//if not found
                right++; 
                count++;
                result = max(result, count);
                wordle.insert(c);
            } else { //if found
                while (s.at(left) != c) { //find the instance where we see the char is c
                    
                    wordle.erase(s.at(left));
                    left++;
                    count--;
                }
                if (s.at(left) == c) { //if found the char c, move the left 1 step more 
                    wordle.erase(c);
                    count--;
                    left++;

                }
                wordle.insert(c);
                count++;
                result = max(result, count);
            }
        }
        return result;
    }
};

/*

s = "zxyzxyz"
     ...

we use hashtable for this
loop throught the string
int count
int result = count;
left and right 0, 0
-----------------------------------------------------
z
    check if it is in the hashtable using .find()

        if not
        add it to the hashtable with key 'z' and value 1 (frequency)
        count++
        result = max(result,count)
        right++

x
    check if it is hashtable
    add it to the hashtable with key 'x' and value 1 (freq)
    count++
    result = max(result,count)
    right++
y
    check if it is hashtable
    add it to the hashtable with key 'y' and value 1 (freq)
    count++
    result = max(result,count)
    right++

-----------------------------------------------------
z
    check if it is in the hashtable using .find()
    yes:
        loop while string.at(i)!='z'
                left++
                c--;
        left++
        c--;
    hashtable map .erase ('z')



*/