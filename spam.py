import praw
import time
import random
import config as cfg

reddit = praw.Reddit(client_id=cfg.reddit_id,
                     client_secret=cfg.reddit_secret,
                     password=cfg.reddit_pass,
                     user_agent=cfg.reddit_user_agent,
                     username=cfg.reddit_user) 

# Gets copypastas
copypastas = []
print('Getting copypastas')
for post in reddit.subreddit('copypasta').top(limit=30):
    if post.is_self: # Only saves the copypastas from self posts
        copypastas.append(post.selftext)

# Spam!
def spam():
    # Goes through the rising posts for potential max visibility
    for post in reddit.subreddit('all').rising():
        # Check if haven't commented on this post recently
        if post not in reddit.user.me().new(limit=5):
            try:
                # Directly reply to post if not many comments already
                if post.num_comments < 15:
                    print('Posting reply to ' + post.permalink)
                    post.reply(random.choice(copypastas))
                # Find the top comment to reply to
                else:
                    # Get comment with highest score
                    best_score = post.comments[0].score
                    best_comm = post.comments[0]
                    for comm in post.comments:
                        if comm.score > best_score:
                            best_score = comm.score
                            best_comm = comm
                    # Reply to top comment
                    print('Posting reply to ' + post.permalink)
                    best_comm.reply(random.choice(copypastas))
                # Wait a minute before doing another comment
                time.sleep(60)
            except praw.exceptions.APIException as e:
                print('Got ratelimited')
                # Wait a little more than 9 minutes to try again
                time.sleep(550)

spam()
