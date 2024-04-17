#include <map>
#include <queue>
#include <string>
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
    string smallestFromLeaf(TreeNode* root) {
        map<TreeNode*, string> mp;
        queue<TreeNode*> q;
        q.push(root);
        mp[root] = string(1, 'a' + root->val);
        string m(8500, 'z');

        while (!q.empty()) {
            TreeNode* c =  q.front();
            q.pop();

            if (!(c->left || c->right)) {
                if (mp[c] < m) {
                    m = mp[c];
                }
            }
            if (c->left) {
                mp[c->left] = char(c->left->val + 'a') + mp[c];
                q.push(c->left);
            }
            if (c->right) {
                mp[c->right] = char(c->right->val + 'a') + mp[c];
                q.push(c->right);
            }
        }
        return m;
    }
};