void dfs(Node* root,int v,vector<int>&lst){
    if(root->left)dfs(root->left,v,lst);
    int x=root->data;
    if(x>=v)lst.push_back(x);
    if(root->right)dfs(root->right,v,lst);
}
int findCeil(Node* root, int input){
    vector<int>lst;
    dfs(root,input,lst);
    if(lst.size()>0)return lst[0];
    return -1;
}
