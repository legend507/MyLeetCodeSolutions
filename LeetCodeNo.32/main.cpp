#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

// Way to think:
//  first observe (, and then observe )
//  need to find a way to follow if any previous ( is observed when observing )

class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stk;
        stk.push(-1);
        int maxL=0;
        for(int i=0;i<s.size();i++)
        {
            int t=stk.top();
            if(t!=-1
                &&s[i]==')'
                &&s[t]=='(')
            {
                stk.pop();
                cout << "i=" << i << endl;
                cout << "t=" << stk.top() << endl;                
                maxL=max(maxL,i-stk.top());
            }
            else
                stk.push(i);
        }
        return maxL;
    }
};

int main() {
    Solution s;
    string array = {"(((((()()"};
    cout << s.longestValidParentheses(array) << endl;
    return 0;
}
