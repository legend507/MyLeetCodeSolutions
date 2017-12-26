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
        int maxans = 0;
        vector<int> maxansArray;        
        int ret = 0;
        stack<int> array;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                array.push(i);
                maxansArray.push_back(maxans);
                maxans = 0;
            } else {
                if(!array.empty()) {
                    maxans = max(maxans, i - array.top()+1);
                    array.pop();
                }
            }
        }

        for(int i = 0; i < maxansArray.size(); i++) {
            ret += maxansArray[i];
        }

        return ret;
    }
};

int main() {
    Solution s;
    string array = {"(()()"};
    cout << s.longestValidParentheses(array) << endl;
    return 0;
}
