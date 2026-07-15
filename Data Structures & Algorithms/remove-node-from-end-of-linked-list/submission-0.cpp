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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        ListNode dummy(0);
        dummy.next = head;
        ListNode* curr = &dummy; 
        int i = 0; 
        ListNode* left = curr; 
        ListNode* right = curr; 
        //getting the offset 
        while (i!=n){
            right= right->next; 
            i++;
        }
        //getting the right k till the right part is nullptr
        while(right->next!=nullptr){
            left=left->next; 
            right=right->next; 
        }
        //assuming the right hit last and left is right before the node that should be removed. 
        left->next = left->next->next; 
        return dummy.next ;
    }
};
