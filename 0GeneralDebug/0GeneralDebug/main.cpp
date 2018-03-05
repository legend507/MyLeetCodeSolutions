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
#include <stack>
using namespace std;

// A BST node
struct node
{
    int data;
    node* left, *right;
    
    node(int x) : data(x), left(NULL), right(NULL) {}
};

class Graph {
public:
    int v;
    list<int> *adj;
    
    Graph(int v) {
        this->v = v;
        adj = new list<int>[v];
    }
    
    void addEdge(int v, int w) {
        adj[v].push_back(w);
    }
    
    void topologicalSortUtil(int v, bool visited[], stack<int>& stack) {
        
    }
    
    void printGraph() {
        for(int i = 0; i < v; i++) {
            for(auto itr=adj[i].begin(); itr != adj[i].end(); itr++) {
                cout << *itr << " " << endl;
            }
            cout << endl;
        }
    }
    
};

class AlienDict {
public:
    void process(vector<string>& words) {
        unordered_map<char, int> record;
        for(auto oneWord:words) {
            for(int i = 0; i < oneWord.size(); i++) {
                record[oneWord[i]] = (int)oneWord[i];
            }
        }
        
        int allLetters = (int)record.size();
        Graph g(allLetters);
        
        for(int i = 0; i < words.size()-1; i++) {
            string word1 = words[i];
            string word2 = words[i+1];
            
            for(int j = 0; j < min(word1.size(), word2.size()); j++) {
                if(word1[j] != word2[j]) {
                    cout << "adj[" << word1[j]-'a' << "]=" <<word2[j]-'a' << endl;
                    g.addEdge(word1[j]-'a', word2[j]-'a');
                    break;
                }
            }
        }
        g.printGraph();
    }
};

int main() {
    
    vector<string> words = { "caa",
        "aaa",
        "aab" };
    AlienDict ad;
    ad.process(words);
    
    return 0;
}
