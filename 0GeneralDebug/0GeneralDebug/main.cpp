/*
 Given a string containing of ‘0’, ‘1’ and ‘?’ wildcard characters, generate all binary strings that can be formed by replacing each wildcard character by ‘0’ or ‘1’.
 
 Input str = "1??0?101"
 Output:
                 10000101
                 10001101
                 10100101
                 10101101
                 11000101
                 11001101
                 11100101
                 11101101
 */

#include <vector>
#include <iostream>
#include <list>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
#include <queue>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <stack>
using namespace std;

// A BST node
//template <typename T>
//struct TreeNode
//{
//    T data;
//    TreeNode* left, *right;
//
//    TreeNode(T x) : data(x), left(NULL), right(NULL) {}
//};

struct TreeNode
{
    char data;
    TreeNode* left, *right;
    
    TreeNode(char x) : data(x), left(NULL), right(NULL) {}
};

class StringGenerator {
    
    
public:
    /*
     The following is my recurse method
     */
    vector<string> recurseMethod(string str) {
        vector<int> index;
        for (int i = 0; i < str.size(); i++)
            if (str[i] == '?')
                index.push_back(i);
        
        vector<string> ret;
        recurseMethod(ret, index, str, 0);
        
        return ret;
    }
    void recurseMethod(vector<string>& ret, vector<int>& index, string str, int pos) {
        // base case
        if(pos == index.size()) {
            ret.push_back(str);
            return;
        }
        
        // recurse case
        str[index[pos]] = '0';
        recurseMethod(ret, index, str, pos+1);
        str[index[pos]] = '1';
        recurseMethod(ret, index, str, pos+1);
    }
};


int main() {
    StringGenerator sg;
    vector<string> ret = sg.recurseMethod("1??0?101");
    
    for(auto oneStr : ret) {
        cout << oneStr << endl;
    }
    
    system("pause");
    return 0;
}

