class Solution {
public:
    bool f(string s,int i){
        if(i==s.size()/2 ) return true;
        if(s[i]!=s[s.size()-1-i]) return false;
        return f(s,i+1);
    }
    bool isPalindrome(int x) {
        return f(to_string(x),0)==true;
    }
};
