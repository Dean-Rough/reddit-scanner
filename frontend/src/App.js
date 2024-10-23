import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [subreddit, setSubreddit] = useState('');
  const [subreddits, setSubreddits] = useState([]);
  const [posts, setPosts] = useState([]);

  // Fetch subreddits from the backend API
  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/subreddits')
      .then(response => response.json())
      .then(data => setSubreddits(data))
      .catch(error => console.error('Error fetching subreddits:', error));
  }, []);

  // Fetch posts from the backend API
  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/posts')
      .then(response => response.json())
      .then(data => setPosts(data))
      .catch(error => console.error('Error fetching posts:', error));
  }, []);

  const addSubreddit = () => {
    if (subreddit && !subreddits.includes(subreddit)) {
      setSubreddits([...subreddits, subreddit]);
      setSubreddit('');
      // Optionally, you can send this new subreddit to the backend to monitor it
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Reddit Sentiment Analyzer</h1>
        <div>
          <input
            type="text"
            value={subreddit}
            onChange={(e) => setSubreddit(e.target.value)}
            placeholder="Enter subreddit name"
          />
          <button onClick={addSubreddit}>Add Subreddit</button>
        </div>
        <h2>Monitored Subreddits:</h2>
        <ul>
          {subreddits.map((sub, index) => (
            <li key={index}>{sub}</li>
          ))}
        </ul>

        <h2>Latest Posts:</h2>
        <ul>
          {posts.map((post, index) => (
            <li key={index}>
              <a href={post.url} target="_blank" rel="noopener noreferrer">
                {post.title}
              </a>
              <p>Score: {post.score}</p>
              <p>Sentiment: {JSON.stringify(post.sentiment)}</p>
            </li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;