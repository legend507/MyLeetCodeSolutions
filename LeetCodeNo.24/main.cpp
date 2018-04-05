/*
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <stack>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode * swapPairs(ListNode* head) {
		if (head == NULL)	return NULL;
		if (head->next == NULL) return head;

		int count = 0;
		ListNode* first = head;
		ListNode* second = head->next;
		head = second;
		ListNode* former = first;

		while (first != NULL && second != NULL) {
			// swap
			first->next = second->next;
			second->next = first;
			if(count!=0) former->next = second;
			// move forward
			former = first;
			first = first->next;
			if (first != NULL) second = first->next;

			count++;
			

		}
		return head;

	}
};

int main()
{

	Solution s;
	ListNode* head = new ListNode(1);
	head->next = new ListNode(2);
	head->next->next = new ListNode(3);
	head->next->next->next = new ListNode(4);
	head->next->next->next->next = new ListNode(5);


	head = s.swapPairs(head);

	while (head != NULL) {
		cout << head->val << "->";
		head = head->next;
	}

	system("pause");
	return 0;
}