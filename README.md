autogpt-twitter 🐣

A plugin adding Twitter API integration into Auto GPT
Features

    Post a tweet using the post_tweet(tweet) command
    Post a reply to a specific tweet using the post_reply(tweet, tweet_id) command
    Get recent mentions using the get_mentions() command
    Search a user's recent tweets via username using the search_twitter_user(targetUser, numOfItems) command
    Send a tweet using the send_tweet(tweet_text) command
    Get a user's tweets using the get_user_tweets(user_id, count=10) command
    Search tweets using the search_tweets(query, count=10) command
    Get trending topics using the get_trending_topics() command
    Follow a user using the follow_user(user_id) command
    Unfollow a user using the unfollow_user(user_id) command
    Send a direct message using the send_direct_message(user_id, message_text) command
    Like a tweet using the like_tweet(tweet_id) command
    Unlike a tweet using the unlike_tweet(tweet_id) command
    Retweet a tweet using the retweet(tweet_id) command
    Unretweet a tweet using the unretweet(tweet_id) command

... and many more!
Installation

    Download this repository, and save it as autogpt-twitter.zip
    Place the .zip file in the plugins directory of your AutoGPT install
    Add your Twitter API information to the .env file within AutoGPT:

makefile

################################################################################
### TWITTER API
################################################################################

# Consumer Keys are also known as API keys on the dev portal

TW_CONSUMER_KEY=
TW_CONSUMER_SECRET=
TW_ACCESS_TOKEN=
TW_ACCESS_TOKEN_SECRET=
TW_CLIENT_ID=
TW_CLIENT_ID_SECRET=

Twitter API Setup

    Go to the Twitter Dev Portal
    Delete any apps/projects that it creates for you
    Create a new project with whatever name you want
    Create a new app under said project with whatever name you want
    Under the app, edit user authentication settings and give it read/write perms.
    Grab the keys listed in installation instructions and save them for later