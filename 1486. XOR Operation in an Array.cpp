class Solution {
public:

    int xorOperation(int n, int start){
        if(n==1) return start;
        return start ^ xorOperation(--n,start+2);
    }
};
