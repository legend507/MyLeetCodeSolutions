/*
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
*/

/*
以下方法是我原创，写的很乱，过了但只beat 2.72%
*/
class Solution {
    int which;
    int num;
    int label;
    string answer, ret;
    bool found;
    int factorial(int n) {
        int ret = 1;
        for(int i = 1; i <= n; i++) ret *= i;
        return ret;
    }
    
    void doRecurse(string& input, vector<bool>& used) {
        // 
        if (answer.size() == num) label ++;
        if (label == which) {found = true; ret = answer;}
        
        for(int i = 0; i < num && !found; i++) {
            // used
            if(used[i]) {
                continue;
            } 
            // NOT used
            else {
                used[i] = true;
                answer += input[i];
                doRecurse(input, used);
                used[i] = false;
                answer = answer.substr(0, answer.size() - 1);
            }
        }
    }
    
public:
    string getPermutation(int n, int k) {
        // input check
        if (n <= 0 || k <= 0) return "";
        if (k > factorial(n)) return "";
        
        which = k;
        num = n;
        label = 0;
        found = false;
        
        // construct input string
        string input;
        for(int i = 1; i <= n; i ++) input += to_string(i);
        
        vector<bool> used(n, false);
        doRecurse(input, used);
        return ret;
    }
};