# Twitter-Crawling

This project aims at crawling data from twitter application using twitter API. In this project user id and post details of users are extracted using API and stored in mysql database.

## System design for Twitter-Crawling
   ![image](https://user-images.githubusercontent.com/115713117/223177891-d4501db4-f6b1-4e5d-9770-d15152c650ce.png)

## Requirements
- requests module
- pymysql
- Twitter login account
- Create a developer account in the Twitter Developer Portal
- Twitter API keys


1. Login to twitter, collect some random twitter_handles and save them in csv file

2. Login to twitter developer account using portal, and get access to Twitter APIv2.
   For more information on how to access to Twitter API refer the following link - https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-   the-twitter-api
    Save your Api keys and tokens in the file

3. Make a request to twitter Api using requests module and collect the user_id of twitter handle and store them in the list.

4. Make a request to twitter Api using requests module and collect the post details of user id and store them in the list.

5. Store the result in mysql database



