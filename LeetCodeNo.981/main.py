# This works, but will cause time limit exceed.
# Didn't solve this one, time limit is a problem. Answer provided by leetcode is also causing time limit error.
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
        self.store[key][timestamp] = value

    def get_slow(self, key: str, timestamp: int) -> str:
        if timestamp in self.store[key]:
            return self.store[key][timestamp]
        else:
            # This part finding is causing the time out issue.
            most_recent_timestamp = self.find_most_recent_timestamp(key, timestamp)
            if most_recent_timestamp == None:
                return ""
            else:
                return self.store[key][most_recent_timestamp]
    
    def find_most_recent_timestamp(self, key, timestamp):
        keys = [i for i, _ in self.store[key].items()]
        keys = sorted(keys)
        if timestamp < keys[0]:
            return None
        for i in range(len(keys) - 1):
            if timestamp >= keys[i] and timestamp < keys[i+1]:
                return keys[i]
        return keys[-1]
    
    def get(self, key: str, timestamp: int) -> str:


        if key not in self.store:
            return ""
        
        # Check if timestamp is larger than max timestamp for a key.
        max_timestamp = max([i for i, _ in self.store[key].items()])
        if timestamp > max_timestamp:
            return self.store[key][max_timestamp]
        
        
        for try_timestamp in range(timestamp, 0, -1):
            if try_timestamp in self.store[key]:
                return self.store[key][try_timestamp]
        return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)