
class Solution{
  public:
    void dfs(Node *root, Node *x,Node *&node,Node *&tmp){
        if(!root)return;
        dfs(root->left,x,node,tmp);
        if(tmp==x) node = root;
        tmp=root;
        if(root->right) dfs(root->right,x,node,tmp);
    }
  public:
    // returns the inorder successor of the Node x in BST (rooted at 'root')
    Node * inOrderSuccessor(Node *root, Node *x){
        //Your code here
        Node *node=NULL;
        Node *tmp=NULL;
        dfs(root,x,node,tmp);
        return node;
    }
};
