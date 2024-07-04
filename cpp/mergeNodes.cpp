

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        recurse(head);
        return head;
    }

    void recurse(ListNode* head) {
        if (!head->next) return;

        int sum = 0;
        ListNode* cur = head->next;
        while (cur->val != 0) {
            sum += cur->val;
            cur = cur->next;
        }

        head->val = sum;
        if (cur->next == nullptr) {
            head->next = nullptr;
        } else {
            head->next = cur;
            recurse(head->next);
        }
    }
};