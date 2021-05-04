import React from 'react';

import { NavLink } from 'react-router-dom';

import Footer from '../../components/footer';
import Header from '../../components/header';
import Navbar from '../../components/navbar'


const Blog = () => {
    return (
        <div class="body-home">
        <Header/>

        
        <main class="main">
        <Navbar/>
            <div class="main__content">
            
                <div class="blog">
                    <h2 class="second-title mb-4">Blogs</h2>
                    <div class="row">
                        <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                            <div class="card-blog">
                                <div class="card-blog__img">
                                    <img src="images/blog-1.jpg" alt="images"/>
                                </div>
                                <div class="card-blog__text">
                                    <span class="title-blog">Titre du blog</span>
                                    <ul>
                                        <li>
                                            <img src="images/icon/user.svg" alt="icone"/>
                                            <span>Admin</span>
                                        </li>
                                        <li>
                                            <img src="images/icon/calendar.svg" alt="icone"/>
                                            <span>19-Avril-2021</span>
                                        </li>
                                    </ul>
                                    <p>
                                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem 
                                        dolor voluptatibus ea blanditiis corporis, officia animi libero perspiciatis, 
                                        quis reiciendis nostrum ...
                                    </p>
                                    <NavLink to="blog-detail">
                                        <button type="button" class="btn-orange">Lire Plus</button>
                                    </NavLink>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                            <div class="card-blog">
                                <div class="card-blog__img">
                                    <img src="images/blog-2.jpg" alt="images"/>
                                </div>
                                <div class="card-blog__text">
                                    <span class="title-blog">Titre du blog</span>
                                    <ul>
                                        <li>
                                            <img src="images/icon/user.svg" alt="icone"/>
                                            <span>Admin</span>
                                        </li>
                                        <li>
                                            <img src="images/icon/calendar.svg" alt="icone"/>
                                            <span>19-Avril-2021</span>
                                        </li>
                                    </ul>
                                    <p>
                                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem 
                                        dolor voluptatibus ea blanditiis corporis, officia animi libero perspiciatis, 
                                        quis reiciendis nostrum ...
                                    </p>
                                    <NavLink to="blog-detail">
                                        <button type="button" class="btn-orange">Lire Plus</button>
                                    </NavLink>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                            <div class="card-blog">
                                <div class="card-blog__img">
                                    <img src="images/blog-3.jpg" alt="images"/>
                                </div>
                                <div class="card-blog__text">
                                    <span class="title-blog">Titre du blog</span>
                                    <ul>
                                        <li>
                                            <img src="images/icon/user.svg" alt="icone"/>
                                            <span>Admin</span>
                                        </li>
                                        <li>
                                            <img src="images/icon/calendar.svg" alt="icone"/>
                                            <span>19-Avril-2021</span>
                                        </li>
                                    </ul>
                                    <p>
                                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem 
                                        dolor voluptatibus ea blanditiis corporis, officia animi libero perspiciatis, 
                                        quis reiciendis nostrum ...
                                    </p>
                                    <NavLink to="blog-detail">
                                        <button type="button" class="btn-orange">Lire Plus</button>
                                    </NavLink>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                            <div class="card-blog">
                                <div class="card-blog__img">
                                    <img src="images/blog-1.jpg" alt="images"/>
                                </div>
                                <div class="card-blog__text">
                                    <span class="title-blog">Titre du blog</span>
                                    <ul>
                                        <li>
                                            <img src="images/icon/user.svg" alt="icone"/>
                                            <span>Admin</span>
                                        </li>
                                        <li>
                                            <img src="images/icon/calendar.svg" alt="icone"/>
                                            <span>19-Avril-2021</span>
                                        </li>
                                    </ul>
                                    <p>
                                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem 
                                        dolor voluptatibus ea blanditiis corporis, officia animi libero perspiciatis, 
                                        quis reiciendis nostrum ...
                                    </p>
                                    <NavLink to="blog-detail">
                                        <button type="button" class="btn-orange">Lire Plus</button>
                                    </NavLink>
                                </div>
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

export default Blog;