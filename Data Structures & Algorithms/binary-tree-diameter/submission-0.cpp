class Solution {
public:
    int best = 0;                       // shared across the whole traversal

    int diameterOfBinaryTree(TreeNode* root) {
        height(root);                   // walks the tree, fills in `best`
        return best;
    }

    int height(TreeNode* root) {
        if (root == nullptr)
            return 0;

        int left = 0;
        int right = 0;
        if (root->left)
            left = 1 + height(root->left);
        if (root->right)
            right = 1 + height(root->right);

        best = max(best, left + right); // diameter turning around at THIS node
        return max(left, right);        // height, for my parent
    }
};