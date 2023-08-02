class Solution {
  public:
    void dfs(Node *root,vector<int>&lst){
        if(root->left)dfs(root->left,lst);
        lst.push_back(root->data);
        if(root->right)dfs(root->right,lst);
    }
  public:
    // Return the Kth smallest element in the given BST
    int KthSmallestElement(Node *root, int k) {
        // add code here.
        vector<int>lst;
        dfs(root,lst);
        if(lst.size()>=k)return lst[k-1];
        return -1;
    }
};
