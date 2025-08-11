class Solution {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {

        vector<long long> powers;
        string binary = bitset<32>(n).to_string();
        
        for (int i = binary.length() - 1; i >= 0; i--) {
            if (binary[i] == '1') {
                powers.push_back(1LL << (binary.length() - 1 - i));
            }
        }
        
        vector<int> ans;
        const int modby = 1e9 + 7;
        
        for (const auto& q : queries) {
            int l = q[0];
            int r = q[1];
            long long product = 1;
            
            for (int i = l; i <= r; i++) {
                product = (product * powers[i]) % modby;
            }
            
            ans.push_back(product);
        }
        
        return ans;
    }
};
