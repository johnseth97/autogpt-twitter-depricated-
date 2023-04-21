"""
This module contains functions for interacting with the Twitter API.
"""
from __future__ import annotations
import pandas as pd
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.environ.get("TW_CONSUMER_KEY")
consumer_secret = os.environ.get("TW_CONSUMER_SECRET")
access_token = os.environ.get("TW_ACCESS_TOKEN")
access_token_secret = os.environ.get("TW_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
def post_tweet(tweet: str) -> str:
    """Posts a tweet to twitter.

    Args:
        tweet (str): The tweet to post.

    Returns:
        str: The tweet that was posted.
    """

    _tweetID = api.update_status(status=tweet)

    return f"Success! Tweet: {_tweetID.text}"


def post_reply(tweet: str, tweet_id: int) -> str:
    """Posts a reply to a tweet.

    Args:
        tweet (str): The tweet to post.
        tweet_id (int): The ID of the tweet to reply to.

    Returns:
        str: The tweet that was posted.
    """

    replyID = api.update_status(
        status=tweet, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True
    )

    return f"Success! Tweet: {replyID.text}"


def get_mentions() -> str | None:
    """Gets the most recent mention.

    Returns:
        str | None: The most recent mention.
    """

    _tweets = api.mentions_timeline(tweet_mode="extended")

    for tweet in _tweets:
        return (
            f"@{tweet.user.screen_name} Replied: {tweet.full_text}"
            f" Tweet ID: {tweet.id}"
        )  # Returns most recent mention

def search_twitter_user(target_user: str, num_of_items: int) -> str:
    """Searches a user's tweets given a number of items to retrive and
      returns a dataframe.

    Args:
        target_user (str): The user to search.
        num_of_items (int): The number of items to retrieve.

    Returns:
        str: The dataframe containing the tweets.
    """

    tweets = tweepy.Cursor(
        api.user_timeline, screen_name=target_user, tweet_mode="extended"
    ).items(num_of_items)

    columns = ["Time", "User", "ID", "Tweet"]
    data = []

    for tweet in tweets:
        data.append(
            [tweet.created_at, tweet.user.screen_name, tweet.id, tweet.full_text]
        )

    df = str(pd.DataFrame(data, columns=columns))

    print(df)

    return df  # Prints a dataframe object containing the Time, User, ID, and Tweet
# Additional functions from the provided code

def send_tweet(tweet_text):
    try:
        api.update_status(tweet_text)
        print("Tweet sent successfully!")
    except (tweepy.RateLimitError, tweepy.TweepError) as e:
        print(f"Error sending tweet in send_tweet(): {e}")
    except Exception as e:
        print(f"Unexpected error in send_tweet(): {e}")


def get_user_tweets(user_id, count=10):
    try:
        tweets = api.user_timeline(user_id=user_id, count=count)
        for tweet in tweets:
            print(f"{tweet.text} - Tweet ID: {tweet.id}")
    except (tweepy.RateLimitError, tweepy.TweepError) as e:
        print(f"Error getting user tweets in get_user_tweets(): {e}")
    except Exception as e:
        print(f"Unexpected error in get_user_tweets(): {e}")


def get_tweet_replies(tweet_id, count=10):
    try:
        replies = api.search_tweets(q="to:{}".format(api.get_status(tweet_id).author.screen_name), since_id=tweet_id, count=count)
        for reply in replies:
            if hasattr(reply, 'in_reply_to_status_id_str'):
                if reply.in_reply_to_status_id_str == tweet_id:
                    print(f"{reply.text} - Reply ID: {reply.id}")
    except (tweepy.RateLimitError, tweepy.TweepError) as e:
        print(f"Error getting tweet replies in get_tweet_replies(): {e}")
    except Exception as e:
        print(f"Unexpected error in get_tweet_replies(): {e}")
        
def get_user_timeline(user_id, count=10):
    try:
        timeline = api.user_timeline(user_id=user_id, count=count)
        for tweet in timeline:
            print(f"{tweet.text} - Tweet ID: {tweet.id}")
    except tweepy.TweepyException as e:
        print("Error getting user timeline: {}".format(e.reason))

def get_trending_topics_by_location(lat, long, count=10):
    try:
        closest_trends = api.trends_closest(lat, long)
        trends = api.trends_place(closest_trends[0]['woeid'])
        for trend in trends[0]['trends'][:count]:
            print(trend['name'])
    except tweepy.TweepyException as e:
        print("Error getting trending topics: {}".format(e.reason))
        
def get_user_mentions(user_id, count=10):
    try:
        mentions = api.mentions_timeline(user_id=user_id, count=count)
        for mention in mentions:
            print(f"{mention.text} - Mention ID: {mention.id}")
    except tweepy.TweepyException as e:
        print("Error getting user mentions: {}".format(e.reason))

def get_user_liked_tweets(user_id, count=10):
    try:
        liked_tweets = api.favorites(user_id=user_id, count=count)
        for tweet in liked_tweets:
            print(f"{tweet.text} - Tweet ID: {tweet.id}")
    except tweepy.TweepyException as e:
        print("Error getting user's liked tweets: {}".format(e.reason))

def get_user_retweets(user_id, count=10):
    try:
        retweets = api.user_timeline(user_id=user_id, count=count, include_rts=True)
        for tweet in retweets:
            if hasattr(tweet, 'retweeted_status'):
                print(f"{tweet.retweeted_status.text} - Retweet ID: {tweet.id}")
    except tweepy.TweepyException as e:
        print("Error getting user's retweets: {}".format(e.reason))

def get_tweet_retweeters(tweet_id, count=10):
    try:
        retweets = api.retweeters(tweet_id, count=count)
        for retweeter_id in retweets:
            user = api.get_user(retweeter_id)
            print(f"{user.name} - Retweeter ID: {user.id}")
    except tweepy.TweepyException as e:
        print("Error getting tweet retweeters: {}".format(e.reason))

def search_users(query, count=10):
    try:
        users = api.search_users(query, count=count)
        for user in users:
            print(f"{user.name} - User ID: {user.id}")
    except tweepy.TweepyException as e:
        print("Error searching for users: {}".format(e.reason))

def get_user_follow_counts(user_id):
    try:
        user = api.get_user(user_id)
        print(f"Followers: {user.followers_count}")
        print(f"Following: {user.friends_count}")
    except tweepy.TweepyException as e:
        print("Error getting user follow counts: {}".format(e.reason))

def get_user_blocked_users(count=10):
    try:
        blocked_users = api.get_blocked_users(count=count)
        for user in blocked_users:
            print(f"{user.name} - User ID: {user.id}")
    except tweepy.TweepyException as e:
        print("Error getting blocked users: {}".format(e.reason))
        


        



