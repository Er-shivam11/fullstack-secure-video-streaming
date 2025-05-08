import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Stream from './Stream';
import Upload from './Upload';
import Header from './Header';
import Footer from './Footer';
import Home from './Home';  // Import the Home component

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />  {/* Set the route for Home page */}
        <Route path="/upload" element={<Upload />} />
        <Route path="/stream/:id" element={<Stream />} />
        {/* Add more routes as necessary */}
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
