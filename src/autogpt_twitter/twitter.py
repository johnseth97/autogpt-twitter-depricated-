import __init__ as cfg
import pandas as pd
import tweepy

_tweetID = []
_tweets = []

# Authenticating to twitter
_auth = tweepy.OAuth1UserHandler(cfg.twitter_consumer_key,
                                 cfg.twitter_consumer_secret,
                                 cfg.twitter_access_token,
                                 cfg.twitter_access_token_secret)

_api = tweepy.API(_auth)
3
_stream = tweepy.Stream(cfg.twitter_api_key, cfg.twitter_api_key_secret,
                        cfg.twitter_access_token,
                        cfg.twitter_access_token_secret)


# Posts a tweet(tweet)
def post_tweet(tweet):

    _tweetID = _api.update_status(status=tweet)

    return f"Success! Tweet: {_tweetID.text}"  # Returns the most recent tweet


# Posts a reply(tweet) to a target(tweet_id).
def post_reply(tweet, tweet_id):

    replyID = _api.update_status(status=tweet, in_reply_to_status_id=tweet_id,
                                 auto_populate_reply_metadata=True)

    return f"Success! Tweet: {replyID.text}"  # Returns the most recent reply


# Gets the most recent mention
def get_mentions():

    _tweets = _api.mentions_timeline(tweet_mode="extended")

    for tweet in _tweets:
        return f"@{tweet.user.screen_name} Replied: {tweet.full_text} Tweet ID: {tweet.id}"  # Returns most recent mention


# Searches a user's tweets given a number of items to retrive and returns a dataframe
def search_twitter_user(targetUser, numOfItems):

    _tweets = tweepy.Cursor(_api.user_timeline, screen_name=targetUser,
                            tweet_mode='extended').items(numOfItems)

    columns = ['Time', 'User', 'ID', 'Tweet']
    data = []

    for tweet in _tweets:
        data.append([tweet.created_at, tweet.user.screen_name,
                     tweet.id, tweet.full_text])

    df = str(pd.DataFrame(data, columns=columns))

    print(df)

    return df  # Prints a dataframe object containing the Time, User, ID, and Tweet
