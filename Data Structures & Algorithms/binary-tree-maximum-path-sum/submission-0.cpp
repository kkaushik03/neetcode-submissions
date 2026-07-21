/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
   public:
    int maxPathSum(TreeNode* root) {
         int best = INT_MIN;
         gain(root, best);
        return best;
    }
    int gain(TreeNode* root, int& best){
        if (root == nullptr)
            return 0;
            int left = max(gain(root->left,  best),0);
            int right = max(gain(root->right,  best),0);
            best=  max(root->val+right+left, best);
            return root->val + max(left, right); 

        
    }
};
