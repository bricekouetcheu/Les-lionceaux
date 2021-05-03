import React from 'react';

import { NavLink } from 'react-router-dom';
import Footer from '../components/footer';
import Header from '../components/header';

import Navbar from '../components/navbar';

const Galerie = () => {
    return (
      <div class="body-home">
      <Header/>
      
      <main class="main">
      
      <Navbar/>
          <div class="main__content">
              <div class="box-galerie">
                  <div>
                      <h2 class="second-title mb-4">Galeries</h2>
                  </div>
                  <div class="row">
                      <div class="col-lg-4 col-md-4 col-sm-6 col-12">
                          <div class="galerie-item height-2">
                              <a data-fancybox="gallery" href="../images/photo/galerie-1.jpg">
                                  <img src="../images/photo/galerie-1.jpg"/>
                              </a>
                          </div>
                          <div class="galerie-item height-1">
                              <a data-fancybox="gallery" href="../images/photo/galerie-2.jpg">
                                  <img src="../images/photo/galerie-2.jpg"/>
                              </a>
                          </div>
                      </div>
                      <div class="col-lg-4 col-md-4 col-sm-6 col-12">
                          <div class="galerie-item height-1">
                              <a data-fancybox="gallery" href="../images/photo/galerie-3.jpg">
                                  <img src="../images/photo/galerie-3.jpg"/>
                              </a>
                          </div>
                          <div class="galerie-item height-1">
                              <a data-fancybox="gallery" href="../images/photo/galerie-4.jpg">
                                  <img src="../images/photo/galerie-4.jpg"/>
                              </a>
                          </div>
                          <div class="galerie-item height-1">
                              <a data-fancybox="gallery" href="../images/photo/galerie-5.jpg">
                                  <img src="../images/photo/galerie-5.jpg"/>
                              </a>
                          </div>
                      </div>
                      <div class="col-lg-4 col-md-4 col-sm-6 col-12">
                          <div class="galerie-item height-1">
                              <a data-fancybox="gallery" href="../images/photo/galerie-6.jpg">
                                  <img src="../images/photo/galerie-6.jpg"/>
                              </a>
                          </div>
                          <div class="galerie-item height-2">
                              <a data-fancybox="gallery" href="../images/photo/galerie-7.jpg">
                                  <img src="../images/photo/galerie-7.jpg"/>
                              </a>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </main>

      <Footer/>
     
    </div>
    );
};

export default Galerie;