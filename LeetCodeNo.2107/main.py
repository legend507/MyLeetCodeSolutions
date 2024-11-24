class Solution:
    def shareCandies_tooSlow(self, candies: List[int], k: int) -> int:
        # My solution. Time limit exceeded.
        N = len(candies)

        if k == 0:
            return len(set(candies))
        if k == N:
            return 0
        
        # Traverse once, find out possible ways to give candies.
        # Store what's left.
        left = []
        for i in range(N):
            if i + k > N:
                break
            left_candies = candies[0:i] + candies[i+k:]
            print(candies[i:i+k], left_candies)
            left.append(len(set(left_candies)))
        return max(left)
    
    def shareCandies(self, candies, k):
        # Editorial solution.
        
        # Store the total number of unique flavors in the array.
        flav_freq = defaultdict(int)
        for c in candies:
            flav_freq[c] += 1

        # Get the total number of unique flavors in the array.
        unique_flav = len(flav_freq)

        # Get the flavors used completely in the window.
        used_in_window = 0
        for i in range(k):
            flav_freq[candies[i]] -= 1
            if flav_freq[candies[i]] == 0:
                used_in_window += 1

        # Get the flavors in the remaining array currently.
        max_flav = unique_flav - used_in_window

        # Slide the window to the right.
        for i in range(k, len(candies)):
            # Remove the candy on the left end from the window.
            flav_freq[candies[i - k]] += 1
            if flav_freq[candies[i - k]] == 1:
                used_in_window -= 1

            # Add the candy on the right end at index i.
            flav_freq[candies[i]] -= 1
            if flav_freq[candies[i]] == 0:
                used_in_window += 1

            max_flav = max(max_flav, unique_flav - used_in_window)

        return max_flav