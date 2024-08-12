#include <vector>
#include <queue>
#include <functional>

using namespace std;

class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> minHeap; // Min-heap
    int k;
    
    KthLargest(int k, vector<int>& nums) : k(k) {
        for (int num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
        minHeap.push(val);
        
        if (minHeap.size() > k) {
            minHeap.pop();
        }
        
        return minHeap.top();
    }
};