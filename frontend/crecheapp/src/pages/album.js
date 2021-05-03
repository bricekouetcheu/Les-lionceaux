import React from 'react';

import { NavLink } from 'react-router-dom';
import Footer from '../components/footer';
import Header from '../components/header';

import Navbar from '../components/navbar';

const Album = () => {
    return (
      <div class="body-home">
      <Header/>

     
      <main class="main">
         <Navbar/>
          <div class="main__content">
     
              <div class="box-galerie">
                  <div>
                      <h2 class="second-title mb-4">Album</h2>
                  </div>
                  <div class="row">
                      <div class="col-lg-3 col-md-4 col-sm-4 col-6">
                          <NavLink to="/galerie">
                              <div class="card-album">
                                  <div class="card-album__img">
                                      <img src="../images/c1.jpeg" alt="images"/>
                                  </div>
                                  <div class="card-album__title">
                                      <h4 class="four-title">Titre de l'album</h4>
                                  </div>
                              </div>
                          </NavLink>
                      </div>
                      <div class="col-lg-3 col-md-4 col-sm-4 col-6">
                          <NavLink to="/galerie">
                              <div class="card-album">
                                  <div class="card-album__img">
                                      <img src="../images/c1.jpeg" alt="images"/>
                                  </div>
                                  <div class="card-album__title">
                                      <h4 class="four-title">Titre de l'album</h4>
                                  </div>
                              </div>
                          </NavLink>
                      </div>
                      <div class="col-lg-3 col-md-4 col-sm-4 col-6">
                          <NavLink to="/galerie">
                              <div class="card-album">
                                  <div class="card-album__img">
                                      <img src="../images/c1.jpeg" alt="images"/>
                                  </div>
                                  <div class="card-album__title">
                                      <h4 class="four-title">Titre de l'album</h4>
                                  </div>
                              </div>
                          </NavLink>
                      </div>
                      <div class="col-lg-3 col-md-4 col-sm-4 col-6">
                          <NavLink to="/galerie">
                              <div class="card-album">
                                  <div class="card-album__img">
                                      <img src="../images/c1.jpeg" alt="images"/>
                                  </div>
                                  <div class="card-album__title">
                                      <h4 class="four-title">Titre de l'album</h4>
                                  </div>
                              </div>
                          </NavLink>
                      </div>

                      <div class="col-lg-3 col-md-4 col-sm-4 col-6">
                          <NavLink to="/galerie">
                              <div class="card-album">
                                  <div class="card-album__img">
                                      <img src="../images/c1.jpeg" alt="images"/>
                                  </div>
                                  <div class="card-album__title">
                                      <h4 class="four-title">Titre de l'album</h4>
                                  </div>
                              </div>
                          </NavLink>
                      </div>
                      <div class="col-lg-3 col-md-4 col-sm-4 col-6">
                          <NavLink to="/galerie">
                              <div class="card-album">
                                  <div class="card-album__img">
                                      <img src="../images/c1.jpeg" alt="images"/>
                                  </div>
                                  <div class="card-album__title">
                                      <h4 class="four-title">Titre de l'album</h4>
                                  </div>
                              </div>
                          </NavLink>
                      </div>
                      <div class="col-lg-3 col-md-4 col-sm-4 col-6">
                          <NavLink to="/galerie.html">
                              <div class="card-album">
                                  <div class="card-album__img">
                                      <img src="../images/c1.jpeg" alt="images"/>
                                  </div>
                                  <div class="card-album__title">
                                      <h4 class="four-title">Titre de l'album</h4>
                                  </div>
                              </div>
                          </NavLink>
                      </div>
                  </div>
              </div>
          </div>
      </main>

      <Footer/>
      
  </div>
    );
};

export default Album;