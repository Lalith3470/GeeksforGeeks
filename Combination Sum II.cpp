
class Solution{
public:
    void combs(int idx,vector<int>arr, int k, vector<int>&tmp,vector<vector<int>>&lst,int sm){
        if(k==sm){
            lst.push_back(tmp);
            return ;
        }
        for(int i=idx;i<arr.size();i++){
            if(arr[i]+sm>k || i>idx && arr[i]==arr[i-1]){
    			continue;
    		}
    		tmp.push_back(arr[i]);
    		combs(i+1,arr,k,tmp,lst,sm+arr[i]);
    		tmp.pop_back();
        }
    }
    vector<vector<int>> CombinationSum2(vector<int> arr,int n,int k)
    {
        //code here
        vector<vector<int>>lst;
        vector<int>tmp;
        sort(arr.begin(),arr.end());
        combs(0,arr,k,tmp,lst,0);
        return lst;
    }
};
