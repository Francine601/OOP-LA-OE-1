class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"Logging in as {self.username}...")

    def post(self, content):
        print(f"Posting content: {content}")

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self, story_content):
        print(f"Sharing story: {story_content}")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, tweet_content):
        print(f"Tweeting: {tweet_content}")

instagram_account = InstagramAccount("insta_user", "password123", 5000)
instagram_account.login()
instagram_account.post("A beautiful sunset!") 
instagram_account.share_story("Here is my story!") 

twitter_account = TwitterAccount("twitter_user", "password456", 1000)
twitter_account.login() 
twitter_account.post("Just posted a new tweet!")  
twitter_account.tweet("This is my first tweet!") 