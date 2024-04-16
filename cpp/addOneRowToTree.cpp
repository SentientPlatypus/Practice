


//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) {
            TreeNode* r = new TreeNode(val, root, nullptr);
            return r;
        }
        modify(root, val, 1, depth);
        return root;
    }   

    void modify(TreeNode* node, int val, int curdepth, int desireddepth) {
        if (curdepth == desireddepth - 1) {
            node->right = new TreeNode(val, nullptr, node->right);
            node->left = new TreeNode(val, node->left, nullptr);
            return;
        }
        else {
            if (node->right) modify(node->right, val, curdepth + 1, desireddepth);
            if (node->left) modify(node->left, val, curdepth + 1, desireddepth);
        }
    }
};