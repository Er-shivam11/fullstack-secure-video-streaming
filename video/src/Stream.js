import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './Stream.css';  // Import the CSS file for styling

function Stream() {
  const { id } = useParams();  // Get the video ID from the URL
  const [videoUrl, setVideoUrl] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchVideo = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/upload/?id=${id}`);
        if (!response.ok) {
          const responseData = await response.json();
          setError(responseData.error || 'Something went wrong.');
          setLoading(false);
          return;
        }

        const videoBlob = await response.blob();  // Convert response to blob (binary data)
        const videoUrl = URL.createObjectURL(videoBlob);  // Create a URL for the video blob
        setVideoUrl(videoUrl);
        setLoading(false);
      } catch (err) {
        setLoading(false);
        setError('Failed to load video.');
        console.error('Error fetching video:', err);
      }
    };

    fetchVideo();
  }, [id]);

  return (
    <div className="stream-container">
      <div className="stream-header">
        <div className="logo">YouTube</div>
        <div className="search-bar">
          <input type="text" placeholder="Search..." />
        </div>
      </div>

      <div className="main-content">
        <div className="video-player">
          {loading ? (
            <p className="loading">Loading video...</p>
          ) : error ? (
            <p className="error">{error}</p>
          ) : (
            <div>
              <h1 className="video-title">Video Title Goes Here</h1>
              <video controls width="100%" height="auto">
                <source src={videoUrl} type="video/mp4" />
                Your browser does not support the video tag.
              </video>
              <div className="video-stats">
                <button className="like-btn">👍 123</button>
                <button className="dislike-btn">👎 45</button>
              </div>
              <div className="comments-section">
                <h3>Comments</h3>
                <p>No comments yet. Be the first to comment!</p>
              </div>
            </div>
          )}
        </div>

        <div className="video-suggestions">
          <div className="suggestion-card">
            <img src="/images/2.jpg" alt="Video Thumbnail" />
            <div className="suggestion-details">
              <h4>Suggested Video Title 1</h4>
              <p>1M views • 2 days ago</p>
            </div>
          </div>
          <div className="suggestion-card">
            <img src="/images/2.jpg" alt="Video Thumbnail" />
            <div className="suggestion-details">
              <h4>Suggested Video Title 2</h4>
              <p>500K views • 5 days ago</p>
            </div>
          </div>
          <div className="suggestion-card">
            <img src="/images/2.jpg" alt="Video Thumbnail" />
            <div className="suggestion-details">
              <h4>Suggested Video Title 3</h4>
              <p>200K views • 1 week ago</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Stream;
