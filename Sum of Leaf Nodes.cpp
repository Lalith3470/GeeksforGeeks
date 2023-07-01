
/*Structure of the node of the binary tree is as
struct Node
{
	int data;
	Node *left, *right;
};*/
// function should return the sum of all the 
// leaf nodes of the binary tree 
void dfs(Node * root,int &sm){
    if(root->left==NULL && root->right==NULL){
        sm+=root->data;
        return;
    }
    if(root->left)dfs(root->left,sm);
    if(root->right)dfs(root->right,sm);
}
int sumLeaf(Node* root)
{
    // Code here
    int sm=0;
    dfs(root,sm);
    return sm;
}
