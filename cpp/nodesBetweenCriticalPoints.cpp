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
        if (!head || !head->next || !head->next->next) return {-1, -1};
        
        int f = -1, l = -1, i = 1;
        int mnd = __INT_MAX__;
        
        ListNode* prev = head;
        head = head->next;
        ListNode* next = head->next;
        
        while (next) {
            if ((head->val > prev->val && head->val > next->val) ||  (head->val < prev->val && head->val < next->val)) {
                
                if (f == -1) {
                    f = i;
                } else {
                    mnd = min(mnd, i - l);
                }
                l = i;
            }
            prev = head;
            head = next;
            next = next->next;
            i++;
        }
        
        if (f == l) return {-1, -1};
        
        int mxd = l - f;
        return {mnd, mxd};
    }
};
