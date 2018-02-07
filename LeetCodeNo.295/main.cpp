#include    <iostream>
#include    <queue>
#include	<functional>
using namespace std;

/*
To build a priority queue,
with a pointer to median
*/
class MedianFinder {
private:
	// Biggest->	|secondHalf + firstHalf|	<-Smallest
	//							pop
	priority_queue<int> firstHalf;
	priority_queue<int, vector<int>, greater<int> > secondHalf;
public:
	/** initialize your data structure here. */
	MedianFinder() {
	}

	void addNum(int num) {
		// decide which to insert
		//	1. if first insertion
		if (firstHalf.empty() && secondHalf.empty()) {
			firstHalf.push(num);
		}
		//	2. if new [the bigger num in firstHalf] > num, put num in firstHalf
		else if (num < firstHalf.top()) {
			firstHalf.push(num);
		}
		else {
			secondHalf.push(num);
		}

		// modify first and second Half, s.t. they have equal size
		while (
			1 < fabs(firstHalf.size() - secondHalf.size())
			) {
			// if firstHalf has more num
			if (firstHalf.size() > secondHalf.size()) {
				secondHalf.push(firstHalf.top());
				firstHalf.pop();
			}
			// if secondHalf has more num
			if (firstHalf.size() < secondHalf.size()) {
				firstHalf.push(secondHalf.top());
				secondHalf.pop();
			}
		}
	}

	double findMedian() {
		if (firstHalf.size() == secondHalf.size()) {
			return (double)(firstHalf.top() + secondHalf.top()) / 2;
		}
		else if (firstHalf.size() > secondHalf.size()) {
			return (double)firstHalf.top();
		}
		else {
			return (double)secondHalf.top();
		}
	}
};

/**
* Your MedianFinder object will be instantiated and called as such:
* MedianFinder obj = new MedianFinder();
* obj.addNum(num);
* double param_2 = obj.findMedian();
*/

int main() {
	MedianFinder mf;
	mf.addNum(1);
	mf.addNum(2);

	cout << mf.findMedian() << endl;

	mf.addNum(3);

	cout << mf.findMedian() << endl;


	system("pause");
	return 0;

}
