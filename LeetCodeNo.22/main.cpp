/*
Google Interview Q

22. Generate Parentheses
DescriptionHintsSubmissionsDiscussSolution
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/

/*以下的方法是我自己的，beat 100%*/
class Solution {
    vector<string> ret;
    int limit;
    
    void doRecurse(string oneResult, int used, stack<char> s) {
        // base case
        if(used == limit) {
            oneResult.append(limit*2-oneResult.size(), ')');
            ret.push_back(oneResult);
            return;
        }
        
        // recurse case
        //  如果前面没有配对的(，则现在只能放(
        if(s.empty()) {
            oneResult += '(';
            used ++;
            s.push('(');
            doRecurse(oneResult, used, s);
        } else {
            // try append (
            oneResult += '(';
            used ++;
            s.push('(');
            doRecurse(oneResult, used, s);
            oneResult = oneResult.substr(0, oneResult.size()-1);
            used --;
            s.pop();
            
            // try append )
            oneResult += ')';
            s.pop();    // 放了),就要把前面用来配对这个)的(给pop出来
            doRecurse(oneResult, used, s);
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        limit = n;
        int used = 0;
        string oneResult;
        stack<char> s;  // s用来存用了（了没有，在用）的时候pop这个stack
        doRecurse(oneResult, used, s);
        return ret;
    }
};