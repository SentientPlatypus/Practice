#include <stack>
using namespace std;

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
    TreeNode* invertTree(TreeNode* root) {
        stack<TreeNode*> s;
        s.push(root);

        while (!s.empty()) {
            TreeNode* cur = s.top();
            s.pop();

            if (cur != nullptr){
                swapkids(cur);

                if (cur->left != nullptr) s.push(cur->left);
                if (cur->right != nullptr) s.push(cur->right);
            }
        }
        return root;
    }

    void swapkids(TreeNode* node) {
        if (node == nullptr) return;
        TreeNode* temp;
        temp = node->left;
        node->left = node->right;
        node->right = temp;
    }
};