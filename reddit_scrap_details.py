import praw
from datetime import datetime

def convert_timestamp(timestamp):
    parsed_date = datetime.utcfromtimestamp(timestamp)
    year = int(parsed_date.year)
    month = int(parsed_date.month)
    day = int(parsed_date.day)
    return datetime(year, month, day)

reddit = praw.Reddit(client_id='XB-qlj1hx0sI1w', client_secret='mWMrTyCMTd8l1UCjA3jsvfALHlA', user_agent='uptime_scrapper')

# get 10 hot posts from the uptimeporn subreddit
dates = []
scores = []
hot_posts = reddit.subreddit('uptimeporn').hot(limit=1000)
ranking_posts = []
# hot_posts = reddit.subreddit('uptimeporn').top('all')
for post in hot_posts:
    dates.append(convert_timestamp(post.created_utc))
    ranking_posts.append([post.title, post.url, post.score])

timeline = sorted(dates)
ranking_posts.sort(key=lambda x:x[2], reverse=True)

with open("top10.txt", "w") as top10:
    for top in ranking_posts[:10]:
        top10.write(top[0].encode("utf8")+'\n')
        top10.write(top[1].encode("utf8")+'\n')
        top10.write(str(top[2]).encode("utf8")+'\n')

with open("bot10.txt", "w") as bot10:
    for bot in ranking_posts[-10:]:
        bot10.write(bot[0].encode("utf8")+'\n')
        bot10.write(bot[1].encode("utf8")+'\n')
        bot10.write(str(bot[2]).encode("utf8")+'\n')
            
    
