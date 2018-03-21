import praw
import config as cfg

reddit = praw.Reddit(client_id=cfg.reddit_id,
                     client_secret=cfg.reddit_secret,
                     password=cfg.reddit_pass,
                     user_agent=cfg.reddit_user_agent,
                     username=cfg.reddit_user)

copypastas = []
print('Getting copypastas')
for post in reddit.subreddit('copypasta').top(limit=30):
    if post.is_self:
        copypastas.append(post.selftext)