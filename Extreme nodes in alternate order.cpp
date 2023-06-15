/*
 A binary tree node has data, pointer to left child
   and a pointer to right child 
struct Node
{
    int data;
    Node* left;
    Node* right;
};
*/
class Solution{
  public:
    /* Function to print nodes of extreme corners
    of each level in alternate order */
    vector<int> ExtremeNodes(Node* root){
        // Your code here
        vector<int>lst;
        list<Node *>Q;
        int cnt=0;
        Q.push_back(root);
        while(!Q.empty()){
            vector<int>l;
            int ln=Q.size();
            for(int i=0; i<ln; i++){
                Node *node=Q.front();
                Q.pop_front();
                if(node){
                    l.push_back(node->data);
                    if(node->left) Q.push_back(node->left);
                    if(node->right) Q.push_back(node->right);
                }
            }
            if(!l.empty()){
                if(cnt%2==0) lst.push_back(l[l.size()-1]);
                else lst.push_back(l[0]);
            }
            cnt++;
        }
        //for(auto i:lst)cout<<i<<' ';
        return lst;
    }
};
