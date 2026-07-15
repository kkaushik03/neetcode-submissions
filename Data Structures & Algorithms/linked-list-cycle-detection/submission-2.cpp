/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        unordered_set<ListNode*> values_seen;
        ListNode* curr = head; 
        while(curr!=nullptr){
            if (values_seen.find(curr)!=values_seen.end()){
                return true;
            }
            else
            {
                values_seen.insert(curr);
            }
            curr=curr->next;
        }
        return false; 
    }
};
