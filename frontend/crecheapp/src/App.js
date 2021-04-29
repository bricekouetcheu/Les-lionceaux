import React, { useEffect } from "react";



import { BrowserRouter as Router, } from "react-router-dom";

import SimpleReactLightbox from 'simple-react-lightbox'





// Fichier Routes
import BaseRouter from './routes'



function App() {



  useEffect(() => {
    // sidebar responsive
    const btnMenu = document.querySelector('.btn-menu');
    const sideBar = document.querySelector('.main__sidebar');

    return btnMenu.addEventListener('click', () => {
      sideBar.classList.toggle('sidebar-responsive');
    })
  });

  return (
    <SimpleReactLightbox>
      <Router>

        <BaseRouter />

      </Router>
    </SimpleReactLightbox>
  );
}

export default App;