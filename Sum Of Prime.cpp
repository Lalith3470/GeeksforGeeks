
public:
    bool isvalid(int val){
        if(val<=1)return false;
        for(int i=2;i<=sqrt(val);i++){
            if(val%i==0)return false;
        }
        return true;
    }
  public:
    vector<int> getPrimes(int N) {
        // code here
        vector<int>lst(2,-1);
        for(int i=1;i<=N/2;i++){
            if(isvalid(i) && isvalid(N-i)){
                lst[0]=i;
                lst[1]=N-i;
                return lst;
            }
        }
        return lst;
    }
};
