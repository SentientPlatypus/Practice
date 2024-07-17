#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> s(to_delete.begin(), to_delete.end());
        vector<TreeNode*> result;

        root = helper(root, s, result);

        if (root) {
            result.push_back(root);
        }

        return result;
    }

private:
    TreeNode* helper(TreeNode* node, unordered_set<int>& s, vector<TreeNode*>& result) {
        if (!node) return nullptr;

        node->left = helper(node->left, s, result);
        node->right = helper(node->right, s, result);

        if (s.count(node->val)) {
            if (node->left) result.push_back(node->left);
            if (node->right) result.push_back(node->right);
            return nullptr;
        }

        return node;
    }
};