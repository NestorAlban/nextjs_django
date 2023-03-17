import React from 'react';
import {Header} from '../Header/page';
import Footer from '../Footer/page';
// import '../styles/components/Layout.css'

const Layout = ({ children }) => {
  return (
    <div className="Main">
      <Header />
        {children}
      <Footer />
    </div>
  );
}

export default Layout;