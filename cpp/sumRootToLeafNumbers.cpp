struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
#include <queue>
#include <unordered_map>
#include <set>
#include <math.h>
#include <iostream>
using namespace std;

class Solution {
public:
    int sumNumbers(TreeNode* node) {
        if (!(node->right || node -> left)) {
            return node->val;
        }

        int sum = 0;
        if (node-> right) {
            node-> right->val = node->val * 10 + node->right->val;
            sum += sumNumbers(node->right);
        }
        if (node-> left) {
            node-> left->val = node->val * 10 + node->left->val;
            sum += sumNumbers(node->left);
        }
        return sum;
    }
};