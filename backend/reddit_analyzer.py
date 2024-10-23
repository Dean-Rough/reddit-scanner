import praw
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Load environment variables
load_dotenv()

# Download NLTK data
nltk.download('vader_lexicon')

# Set up Reddit API connection
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

# Connect to MongoDB
mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
client = MongoClient(mongodb_uri)
db = client.reddit_sentiment

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def get_monitored_subreddits():
    subreddits = db.subreddits.find()
    return [sub['name'] for sub in subreddits]

def get_top_posts(subreddit_name, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = subreddit.top(limit=limit)
    
    collection = db.top_posts
    for post in top_posts:
        sentiment = sia.polarity_scores(post.title)
        post_data = {
            "title": post.title,
            "score": post.score,
            "url": post.url,
            "sentiment": sentiment
        }
        collection.insert_one(post_data)
        print(f"Title: {post.title}")
        print(f"Score: {post.score}")
        print(f"Sentiment: {sentiment}")
        print(f"URL: {post.url}")
        print("---")

if __name__ == "__main__":
    subreddits = get_monitored_subreddits()
    if not subreddits:
        print("No subreddits to monitor. Please add subreddits to the database.")
    else:
        for sub in subreddits:
            print(f"Fetching top posts from r/{sub}")
            get_top_posts(sub, 5)
