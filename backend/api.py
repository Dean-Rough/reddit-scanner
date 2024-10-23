from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
client = MongoClient(mongodb_uri)
db = client.reddit_sentiment

@app.route('/api/subreddits', methods=['GET'])
def get_subreddits():
    # Fetch list of subreddits being monitored
    subreddits = db.subreddits.find()
    subreddit_list = [sub['name'] for sub in subreddits]
    return jsonify(subreddit_list)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    # Fetch posts from the database
    posts = db.top_posts.find().limit(100)
    post_list = []
    for post in posts:
        post['_id'] = str(post['_id'])  # Convert ObjectId to string
        post_list.append(post)
    return jsonify(post_list)

if __name__ == '__main__':
    app.run(debug=True)