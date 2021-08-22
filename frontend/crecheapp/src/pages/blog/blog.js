import React, { Component } from 'react';
import {Link} from 'react-router-dom'

//Components
import Header from '../../components/header/Header'
import Sidebar from '../../components/sidebar/Sidebar'
import {Footer} from '../../components/footer/Footer'

//Images
import Blog1 from "../../assets/images/blog-1.jpg"
import Blog2 from "../../assets/images/blog-2.jpg"
import Blog3 from "../../assets/images/blog-3.jpg"
import UserImg from '../../assets/images/icon/user.svg'
import CalendarImg from '../../assets/images/icon/calendar.svg'

class Blog extends Component {
    render() {
        return (
            <div className="body-home">
                {/* Header */}
                <Header title="Crèche les lionceaux" />
                <main className="main">
                    <Sidebar/>
                    {/* blog  */}
                    <div className="main__content">
                        <div class="blog">
                            <h2 class="second-title mb-4">Blogs</h2>
                            <div class="row">
                                <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                                    <div class="card-blog">
                                        <div class="card-blog__img">
                                            <img src={Blog1} alt="images" />
                                        </div>
                                        <div class="card-blog__text">
                                            <span class="title-blog">Titre du blog</span>
                                            <ul>
                                                <li>
                                                    <img src={UserImg} alt="icone" />
                                                    <span>Admin</span>
                                                </li>
                                                <li>
                                                    <img src={CalendarImg} alt="icone" />
                                                    <span>19-Avril-2021</span>
                                                </li>
                                            </ul>
                                            <p>
                                                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem
                                                dolor voluptatibus ea blanditiis corporis, officia animi libero perspiciatis,
                                                quis reiciendis nostrum ...
                                            </p>
                                            <Link to="/blog/1">
                                                <button type="button" class="btn-orange">Lire Plus</button>
                                            </Link>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                                    <div class="card-blog">
                                        <div class="card-blog__img">
                                            <img src={Blog2} alt="images" />
                                        </div>
                                        <div class="card-blog__text">
                                            <span class="title-blog">Titre du blog</span>
                                            <ul>
                                                <li>
                                                    <img src={UserImg} alt="icone" />
                                                    <span>Admin</span>
                                                </li>
                                                <li>
                                                    <img src={CalendarImg} alt="icone" />
                                                    <span>19-Avril-2021</span>
                                                </li>
                                            </ul>
                                            <p>
                                                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem
                                                dolor voluptatibus ea blanditiis corporis, officia animi libero perspiciatis,
                                                quis reiciendis nostrum ...
                                            </p>
                                            <Link to="/blog/1">
                                                <button type="button" class="btn-orange">Lire Plus</button>
                                            </Link>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                                    <div class="card-blog">
                                        <div class="card-blog__img">
                                            <img src={Blog3} alt="images" />
                                        </div>
                                        <div class="card-blog__text">
                                            <span class="title-blog">Titre du blog</span>
                                            <ul>
                                                <li>
                                                    <img src={UserImg} alt="icone" />
                                                    <span>Admin</span>
                                                </li>
                                                <li>
                                                    <img src={CalendarImg} alt="icone" />
                                                    <span>19-Avril-2021</span>
                                                </li>
                                            </ul>
                                            <p>
                                                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem
                                                dolor voluptatibus ea blanditiis corporis, officia animi libero perspiciatis,
                                                quis reiciendis nostrum ...
                                            </p>
                                            <Link to="/blog/1">
                                                <button type="button" class="btn-orange">Lire Plus</button>
                                            </Link>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                                    <div class="card-blog">
                                        <div class="card-blog__img">
                                            <img src={Blog1} alt="images" />
                                        </div>
                                        <div class="card-blog__text">
                                            <span class="title-blog">Titre du blog</span>
                                            <ul>
                                                <li>
                                                    <img src={UserImg} alt="icone" />
                                                    <span>Admin</span>
                                                </li>
                                                <li>
                                                    <img src={CalendarImg} alt="icone" />
                                                    <span>19-Avril-2021</span>
                                                </li>
                                            </ul>
                                            <p>
                                                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem
                                                dolor voluptatibus ea blanditiis corporis, officia animi libero perspiciatis,
                                                quis reiciendis nostrum ...
                                            </p>
                                            <Link to="/blog/1">
                                                <button type="button" class="btn-orange">Lire Plus</button>
                                            </Link>
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
    }
}

export default Blog;