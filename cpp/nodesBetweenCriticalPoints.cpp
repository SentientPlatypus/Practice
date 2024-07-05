#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int mxd = -1;
        int mnd = __INT_MAX__;

        int counter = 0;
        int prev = head->val;

        head = head->next;
        while (head->next != nullptr) {
            
            if ((prev < head->val && head->next->val < head->val) || (prev > head->val && head->next->val > head->val)) {
                mxd = max(counter, mxd);
                mnd = min(counter, mnd);
                counter = 0;
            } else {
                counter ++;
            }
            head = head->next;

        }

        if (mxd != -1) {
            if (mnd == __INT_MAX__) {
                mnd = mxd;
            } 
        } else {
            mnd = -1;
        }
        return {mnd, mxd};
    }
};