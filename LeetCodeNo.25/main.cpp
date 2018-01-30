#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};


// This solution should have O(n) time complixity, and MAYBE O(1) space complexity
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        bool reachEnd = false;
        ListNode* ptr = head;
        ListNode** nodeArray = new ListNode*[k];


        while(ptr != NULL) {
// 1st, put necessary k element pointers into nodeArray
            for(int i = 0; i < k; i++) {
                nodeArray[i] = ptr;
                ptr = ptr->next;
                if(ptr==NULL && i != k-1) {
                    reachEnd = true;
                    break;
                }
            }
// 2nd, sway the pointed values  
            if(!reachEnd) {
                for(int i = 0; i < k/2; i++) {
                   swap((nodeArray[i]->val), (nodeArray[k-1-i]->val));
                }
            }
        }
        delete nodeArray;
        return head;
    }
};

int main() {
    Solution s;
    ListNode ln0(0);
    ListNode ln1(1);

    ln0.next = &ln1;

    ListNode* head = &ln0;

    while(head != NULL) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;

    head = &ln0;
    s.reverseKGroup(head, 2);

    while(head != NULL) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;

    return 0;
}

