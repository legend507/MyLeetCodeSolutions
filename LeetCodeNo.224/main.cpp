#include <iostream>
#include <string>
#include <stack>
using namespace std;

/***********************************/
//  Input only includes: +, -, 0~9, (, ),  ,
//  

//  The Method is:
//      calculate every (),
//          if meet (, stack current sum and the sign of THIS ()
//          if meet ), pop former sum and the sign, sum both

class Solution {
public:
    int calculate(string s) {
        int oneNumber = 0;
        int oneSign = 1;
        stack<int> rets, signForRets;
        int ret = 0;

        for(auto oneChar:s) {

            if(isdigit(oneChar)) {
                oneNumber = oneNumber * 10 + oneChar - '0';
            }            
            // if s[i] is not a number, need to push current oneNumber to vector
            else {
                // 
                ret += oneNumber * oneSign;
                oneNumber = 0;

                switch(oneChar) {
                    case '+':   oneSign = 1;    break;
                    case '-':   oneSign = -1;   break;
                    case '(':   
                        // put current ret and oneSign into stack
                        rets.push(ret);
                        signForRets.push(oneSign);
                        //reset ret and oneSign to calculate whatever is in ()
                        ret = 0;
                        oneSign = 1;
                        break;
                    case ')':   
                        // get ret before (, and then sum with values in ()
                        ret = rets.top() + ret * signForRets.top();
                        
                        rets.pop();
                        signForRets.pop();
                        break;
                }
            }
        }
        ret += oneNumber * oneSign;

        return ret;
    }
};


int main() {
    Solution s;
    cout << s.calculate("(101+(4+5+2)-3)-(6+8-5) - 1");

    return 0;

}

