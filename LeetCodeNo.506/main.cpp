class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        int N = score.size();
        
        // Priority queue elements with "higher priority" is always on the top of the queue.
        priority_queue<pair<int, int>> heap;
        for (int i = 0; i < N; i++) {
            // By default, pair is ranked by the first element in the pair.
            heap.push(make_pair(score[i], i));
        }

        // Create return;
        vector<string> rank(N);
        int place = 1;
        while (!heap.empty()) {
            pair<int, int> current = heap.top();
            heap.pop();

            if(1==place) {
                rank[current.second] = "Gold Medal";
            } else if (2==place) {
                rank[current.second] = "Silver Medal";
            } else if (3==place) {
                rank[current.second] = "Bronze Medal";
            } else {
                rank[current.second] = to_string(place);
            }

            place ++;
        }

        return rank;
    }
};