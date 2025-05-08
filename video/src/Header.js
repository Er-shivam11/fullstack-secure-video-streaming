// Header.js
import React from 'react';
import './Header.css';

function Header() {
  return (
    <header className="ott-header">
      <h2>StreamX</h2>
      <nav>
        <a href="/">Home</a>
        <a href="/upload">Upload</a>
      </nav>
    </header>
  );
}

export default Header;
