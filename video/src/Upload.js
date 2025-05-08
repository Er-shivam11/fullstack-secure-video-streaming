import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Upload.css';  // Import your custom CSS

function Upload() {
  const [videoFile, setVideoFile] = useState(null);
  const [title, setTitle] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleUpload = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    if (!videoFile) {
      setError('Please select a video file to upload.');
      setLoading(false);
      return;
    }

    const formData = new FormData();
    formData.append('file', videoFile);
    formData.append('title', title || 'Untitled');

    try {
      const response = await fetch('http://127.0.0.1:8000/api/upload/', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      if (response.ok) {
        navigate(`/stream/${data.id}`);
      } else {
        setError(data.error || 'Upload failed.');
      }
    } catch (err) {
      setError('Server error. Please try again later.');
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <div className="card">
        <div className="card-body">
          <h2 className="card-title">🎬 Upload Your Video</h2>
          <form onSubmit={handleUpload}>
            <div>
              <label className="form-label">Video Title</label>
              <input
                type="text"
                className="form-control"
                placeholder="e.g., My OTT Short Film"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
              />
            </div>

            <div>
              <label className="form-label">Choose Video File</label>
              <input
                type="file"
                className="form-control"
                accept="video/*"
                onChange={(e) => setVideoFile(e.target.files[0])}
              />
            </div>

            <div className="d-grid">
              <button className="btn-primary" type="submit" disabled={loading}>
                {loading ? 'Uploading...' : 'Upload & Stream ▶️'}
              </button>
            </div>
          </form>

          {error && <div className="alert">{error}</div>}
        </div>
      </div>
    </div>
  );
}

export default Upload;
