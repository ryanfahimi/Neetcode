# 981. Time Based Key-Value Store
# Medium

# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"


# Constraints:


# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.
class TimeMap:

    def __init__(self):
        self.timestamps = {}

    # Time: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = []
        self.timestamps[key].append((timestamp, value))

    # Time: O(logn)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""
        values = self.timestamps[key]
        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return values[right][1] if right >= 0 else ""

    # Your TimeMap object will be instantiated and called as such:
    # obj = TimeMap()
    # obj.set(key,value,timestamp)
    # param_2 = obj.get(key,timestamp)

    def main(self):
        print(f"Command: TimeMap()")
        timeMap = TimeMap()
        print(f"Command: timeMap.set('foo', 'bar', 1)")
        timeMap.set("foo", "bar", 1)
        print(f"Command: timeMap.get('foo', 1)")
        print(f"Output: {timeMap.get('foo', 1)}")
        print(f"Command: timeMap.get('foo', 3)")
        print(f"Output: {timeMap.get('foo', 3)}")
        print(f"Command: timeMap.set('foo', 'bar2', 4)")
        timeMap.set("foo", "bar2", 4)
        print(f"Command: timeMap.get('foo', 4)")
        print(f"Output: {timeMap.get('foo', 4)}")
        print(f"Command: timeMap.get('foo', 5)")
        print(f"Output: {timeMap.get('foo', 5)}")


if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.main()
