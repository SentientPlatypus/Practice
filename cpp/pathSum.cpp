#include <queue>
#include <unordered_map>
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
    bool hasPathSum(TreeNode* root, int targetSum) {
        unordered_map<TreeNode*, int> mp;
        queue<TreeNode*> q;
        q.push(root);
        if (root != nullptr) mp[root] = root->val;

        while (!q.empty()) {
            TreeNode* cur = q.front();
            q.pop();

            //check if leaf path
            if (cur != nullptr) {
                if (cur->left == nullptr && cur->right == nullptr && mp[cur] == targetSum) return true;
                
                if (cur->left != nullptr) {
                    q.push(cur->left);
                    mp[cur->left] = mp[cur] + cur->left->val;
                }
                if (cur->right != nullptr) {
                    q.push(cur->right);
                    mp[cur->right] = mp[cur] + cur->right->val;
                }
            }
        }
        return false;
    }
};