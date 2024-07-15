#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> nodes;
        unordered_set<int> children;


        for (auto desc : descriptions) {
            int p = desc[0];
            int c = desc[1];
            int left = desc[2];

            children.insert(c);

            if (nodes.find(p) == nodes.end()) {
                nodes[p] = new TreeNode(p);
            }
            if (nodes.find(c) == nodes.end()) {
                nodes[c] = new TreeNode(c);
            }


            if (left) nodes[p]->left = nodes[c];
            else nodes[p]->right = nodes[c];
        }


        TreeNode* root = nullptr;
        for (auto& pair : nodes) {
            if (children.find(pair.first) == children.end()) {
                root = pair.second;
                break;
            }
        }
        return root;
    }
};
