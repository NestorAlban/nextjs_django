import React from 'react';
// import { useNavigate } from 'react-router-dom';
import Link from 'next/link';
// import AppContext from '../context/AppContext';
import '../styles/Header.css'

export function Header ()  {

  // const navigate = useNavigate()
  // const homeHandle = () => navigate('/');
  // const parentHandle = () => navigate('/');

  return (
    <nav className="Header">
      <div className="Header-title">
        <Link href="/" className='Header-title_link'>
          {/* <button type='button' className='Header-title_button'>NB Academy</button> */}
          NB Academy
        </Link>
      </div>
      <div className="Header-profile">
        <Link href="/" className='Header-profile_link'>
          Parent user
        </Link>
      </div>
    </nav>
  );
}


