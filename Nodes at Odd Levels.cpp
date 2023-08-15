class Solution
{
public:
    vector<Node *> nodesAtOddLevels(Node *root){
        //code here
        vector<Node *>lst;
        queue<Node*>q;
        int lvl=1;
        q.push(root);
        while(!q.empty()){
            int ln=q.size();
            for(int i=0; i<ln; i++){
                Node *tmp=q.front();
                q.pop();
                if(tmp){
                    if(lvl%2!=0) lst.push_back(tmp);
                    if(tmp->left)q.push(tmp->left);
                    if(tmp->right)q.push(tmp->right);
                }
            }
            lvl++;
        }
        return lst;
    }
};
