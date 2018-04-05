/*
You are given an array A consisting of the integers −1, 0 and 1. A slice of that array is any pair of integers (P, Q) such that 0 ≤ P ≤ Q < N. Your task is to find the longest slice of A whose elements yield a non-negative sum.

Write a function:

int solution(vector<int> &A);

that, given an array A of length N, consisting only of the values −1, 0, 1, returns the length of the longest slice of A that yields a non-negative sum. If there's no such slice, your function should return 0.

For example, given A = [−1, −1, 1, −1, 1, 0, 1, −1, −1], your function should return 7, as the slice starting at the second position and ending at the eighth is the longest slice with a non-negative sum.

For another example, given A = [1, 1, −1, −1, −1, −1, −1, 1, 1] your function should return 4: both the first four elements and the last four elements of array A are longest valid slices.

Assume that:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1..1].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).*/

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <stack>
#include <unordered_set>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	int solution(vector<int> &A) {
		// write your code in C++14 (g++ 6.2.0)
		int size = A.size();
		int sum = 0;

		int curMax = 0;
		int ret = 0;
		for (int i = 0; i < size; i++) {
			if (sum + A[i] >= 0) {
				curMax++;
				sum += A[i];
			}
			// A[i] must be -1
			else {
				ret = max(ret, curMax);
				curMax = 0;
				sum = 0;
			}
		}


		return max(ret, curMax);
	}
};

int main()
{

	vector<int> input = { 0, -1, 0, 0, 1, 0, -1, -1 };
	Solution s;

	cout << s.solution(input);
	

	system("pause");
	return 0;
}

