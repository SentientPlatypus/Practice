#include <vector>
#include <algorithm>
using namespace std;

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
    int countPairs(TreeNode* root, int distance) {
        int count = 0;
        vector<int> distances = dfs(root, distance, count);
        return count;
    }

private:
    vector<int> dfs(TreeNode* node, int distance, int& count) {
        if (!node) return {};

        if (!node->left && !node->right) {
            return {1}; // This is a leaf node, distance to itself is 1
        }

        vector<int> leftDistances = dfs(node->left, distance, count);
        vector<int> rightDistances = dfs(node->right, distance, count);

        // Count good leaf node pairs between left and right children
        for (int l : leftDistances) {
            for (int r : rightDistances) {
                if (l + r <= distance) {
                    count++;
                }
            }
        }

        // Merge distances
        vector<int> mergedDistances;
        for (int l : leftDistances) {
            if (l + 1 < distance) {
                mergedDistances.push_back(l + 1);
            }
        }
        for (int r : rightDistances) {
            if (r + 1 < distance) {
                mergedDistances.push_back(r + 1);
            }
        }

        return mergedDistances;
    }
};
