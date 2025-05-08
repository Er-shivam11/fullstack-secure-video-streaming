import React, { useEffect, useState } from 'react'; 
import './Home.css'; 
// import Features from '../../components/Features/Features';
// import Testimonials from '../../components/Testimonials/Testimonials';

const images = [ 
    '/images/2.jpg',
    '/images/1.jpg',
];

const Home = (props) => {
    const [currentImageIndex, setCurrentImageIndex] = useState(0); 

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentImageIndex((prevIndex) => (prevIndex + 1) % images.length);
        }, 5000); 
        return () => clearInterval(interval); 
    }, []);

    const texts = [ 
        'Welcome to the Streaming',
        'Detecting Damage in Real-Time',
        'Ensuring Safety by Bus Damage Detection',
    ];

    return (
        <div className="container" style={{ backgroundImage: `url(${images[currentImageIndex]})` }}>
            <div className="content">
                <h2 className="title">
                    {texts[currentImageIndex]} {props.username ? `, ${props.username}` : '!!'}
                </h2>
                <button className="cta-button">Get Started</button>
            </div>
        </div>
    );
}

export default Home;
