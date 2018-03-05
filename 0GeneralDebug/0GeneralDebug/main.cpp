/*
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

Examples:

Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa"
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'
*/

#include <vector>
#include <iostream>
#include <list>
#include <string>
#include <unordered_map>
#include <sstream>
#include <queue>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <windows.h>
using namespace std;

// A BST node
struct node
{
	int data;
	node* left, *right;

	node(int x) : data(x), left(NULL), right(NULL) {}
};

class AlianDict {
	/*
	for every word in words
		word[0] <- weight
		for every letter in word
			if letter already found, do nothing
			if letter not found, record & assign weight 0
		if next word[0] == word[0]
			loop compare every letter, until found a different pair
				if found, 
	*/

public:
	vector<char> guessDict(vector<string>& words) {
		unordered_map<char, int> record;
		vector<char> foundLetter;
		// traverse, 2 purposes
		//	1. record all distinguish letters
		//	2. assign weight to initial letters of each word
		char curInitial = NULL;
		int curWeight = 0;
		for (int i = 0; i < words.size(); i++) {
			// meet a new initial
			if (curInitial != words[i][0]) {
				curInitial = words[i][0];
				record[curInitial] = ++curWeight;
				foundLetter.push_back(curInitial);
			}

			// traverse all letters in a word, assign weight=0 to a new word
			for (int j = 1; j < words[i].size(); j++) {
				if (record.find(words[i][j]) == record.end()) {
					record[words[i][j]] = -1;
				}
			}
		}



		for (auto oneChar : record) {
			cout << oneChar.first << "=" << oneChar.second << endl;
		}

		vector<char> ret;
		return ret;
	}

};

int main() {
	unordered_map<char, int> test;
	test['a'] = 1;
	cout << test['b'] << endl;	// output is 0

	AlianDict	ad;
	vector<string> words = { "wrt",
		"wrf",
		"er",
		"ett",
		"rftt" };

	ad.guessDict(words);

	system("pause");
	return 0;
}