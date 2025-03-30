import heapq
from collections import defaultdict
from typing import List

# 355. Design Twitter
# Medium

# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.


# Constraints:


# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
# A user cannot follow himself.
class Twitter:

    # Time: O(1)
    # Space: O(1)
    def __init__(self):
        # Initialize the Twitter object with a dictionary to store tweets and a set to track followers
        self.tweets = defaultdict(list)  # Dictionary to store tweets for each user
        self.followers = defaultdict(set)  # Dictionary to store followers for each user
        self.time = 0  # Variable to track the time of tweet posting

    # Time: O(1)
    # Space: O(m)
    def postTweet(self, user_id: int, tweet_id: int) -> None:
        # Store the tweet with the current time and decrement the time
        self.tweets[user_id].append((self.time, tweet_id))
        self.time -= 1

        # Ensure that the list of tweets does not exceed 10 tweets
        if len(self.tweets[user_id]) > 10:
            self.tweets[user_id].pop(0)

    # Time: O(n)
    # Space: O(k)
    def getNewsFeed(self, user_id: int) -> List[int]:
        # Min-heap to store the tweets
        min_heap = []

        # Collect the most recent tweet from each followee and the user themselves
        for followee_id in self.followers[user_id] | {user_id}:
            if followee_id in self.tweets:
                index = len(self.tweets[followee_id]) - 1
                time, tweet_id = self.tweets[followee_id][index]
                heapq.heappush(min_heap, (time, tweet_id, followee_id, index - 1))

        # Retrieve up to 10 most recent tweets
        news_feed = []
        while min_heap and len(news_feed) < 10:
            time, tweet_id, followee_id, index = heapq.heappop(min_heap)
            news_feed.append(tweet_id)

            # If there are more tweets from this followee, add the next most recent one
            if index >= 0:
                next_time, next_tweet_id = self.tweets[followee_id][index]
                heapq.heappush(
                    min_heap, (next_time, next_tweet_id, followee_id, index - 1)
                )

        return news_feed

    # Time: O(1)
    # Space: O(k)
    def follow(self, follower_id: int, followee_id: int) -> None:
        self.followers[follower_id].add(followee_id)

    # Time: O(1)
    # Space: O(k)
    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if follower_id in self.followers:
            self.followers[follower_id].discard(followee_id)

    def main(self):
        print("Command: Twitter()")
        twitter = Twitter()
        print("Command: postTweet(1, 5)")
        twitter.postTweet(1, 5)
        print("Command: getNewsFeed(1)")
        print(f"Output: {twitter.getNewsFeed(1)}")
        print("Command: follow(1, 2)")
        twitter.follow(1, 2)
        print("Command: postTweet(2, 6)")
        twitter.postTweet(2, 6)
        print("Command: getNewsFeed(1)")
        print(f"Output: {twitter.getNewsFeed(1)}")
        print("Command: unfollow(1, 2)")
        twitter.unfollow(1, 2)
        print("Command: getNewsFeed(1)")
        print(f"Output: {twitter.getNewsFeed(1)}")


if __name__ == "__main__":
    Twitter().main()
