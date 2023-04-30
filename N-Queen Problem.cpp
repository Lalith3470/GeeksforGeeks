
class Solution{
public:
    bool isSafe(int row, int col, int n, vector<string>board){
        int i=row;
        int j=col;
        while(row>=0 && col >=0){
            if(board[row][col]=='Q') return false;
            col--;row--;
        }
        row=i;
        col=j;
        while(col>=0){
            if(board[row][col]=='Q') return false;
            col--;
        }
        row=i;
        col=j;
        while(row<n && col>=0){
            if(board[row][col]=='Q') return false;
            row++;
            col--;
        }
        return true;
    }
public:
    void solve(int col,int n, vector<string>&board,vector<vector<int>>&lst){
        if(col==n){
            vector<int>placed;
            for(int i=0; i<n; i++){
                placed.push_back(board[i].find('Q',0)+1);
            }
            lst.push_back(placed);
            return;
        }
        for(int row=0;row<n;row++){
            if(isSafe(row,col,n,board)){
                board[row][col]='Q';
                solve(col+1,n,board,lst);
                board[row][col]='.';
            }
        }
    }
public:
    vector<vector<int>> nQueen(int n) {
        // code here
        vector<string>board(n);
        string s(n,'.');
        for(int i=0; i<n;i++){
            board[i]=s;
        }
        vector<vector<int>>lst;
        solve(0,n,board,lst);
        sort(lst.begin(),lst.end());
        return lst;
    }
};
