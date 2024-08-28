#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        vector<pair<int,double>> adj[n];
        for(int i=0;i<edges.size();i++){
            adj[edges[i][0]].push_back({edges[i][1],succProb[i]});
            adj[edges[i][1]].push_back({edges[i][0],succProb[i]});
        }
        vector<double> prob(n,0.0);
        prob[start]=1.0;
        queue<pair<int,double>> q;
        q.push({start,1.0});
        while(!q.empty()){
            auto it = q.front();
            q.pop();
            for(auto v:adj[it.first]){
                if(prob[v.first]<(it.second*v.second)){
                    prob[v.first]=it.second*v.second;
                    q.push({v.first,prob[v.first]});
                }
            }
        }
        return prob[end];
    }
};