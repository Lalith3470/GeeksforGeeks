class Solution {
  public:
    void comb(vector<int> &arr, int val, int idx, int sum, vector<int> &tmp, vector<vector<int>> &lst) {
    	if(sum == val) {
    		lst.push_back(tmp);
    		return;
    	}
    	for (int i = idx; i < arr.size(); i++) {
    		if(arr[i] + sum > val) {
    			continue;
    		}
    		if(i > idx && arr[i] == arr[i - 1]) {
    			continue;
    		}
    		tmp.push_back(arr[i]);
    		comb(arr, val, i + 1, sum + arr[i], tmp, lst);
    		tmp.pop_back();
    	}
    }
    vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {
        // Write your code here
        vector<int>tmp;
        vector<vector<int>>lst;
        sort(candidates.begin(),candidates.end());
        comb(candidates,target,0,0,tmp,lst);
        return lst;
    }
    
};
