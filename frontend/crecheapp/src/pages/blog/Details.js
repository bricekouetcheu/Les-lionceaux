import React, { Component } from 'react';


//Components
import Header from '../../components/header/Header'
import Sidebar from '../../components/sidebar/Sidebar'
import {Footer} from '../../components/footer/Footer'

import Galerie2 from '../../assets/images/photo/galerie-2.jpg'

class BlogDetails extends Component {
    render() {
        return (
            <div className="body-home">
                {/* Header */}
                <Header title="Crèche les lionceaux" />
                <main className="main">
                    <Sidebar/>
                    <div class="main__content">
                        {/* <!-- blog --> */}
                        <div class="blog">
                            <h2 class="second-title mb-4">Blog detail</h2>
                            <div class="blog-img">
                                <img src={Galerie2} alt="image" />
                            </div>
                            <div class="blog-text">
                                <h3 class="third-title">Titre du blog</h3>
                                <ul>
                                    <li><strong>Auteur </strong>: Zed Junior</li>
                                    <li><strong>Date </strong>: 18/04/2021</li>
                                </ul>
                                <p>
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil accusantium velit,
                                    nobis similique, magnam eligendi laudantium tempore aperiam beatae corrupti perferendis,
                                    fugiat vero odio ut amet numquam. Ducimus, totam illo?
                                    Dolores ullam delectus fuga dolore ex deserunt non accusantium reiciendis consequuntur
                                    minus nam, quam quidem earum illo? Dolorum libero voluptas cumque harum aut minima
                                    consequuntur
                                    magni, nemo vero eligendi distinctio?
                                    Labore rerum voluptate minima architecto sapiente dolorem illum in delectus ipsa suscipit!
                                    Ea tempore quae magnam nostrum porro eveniet rem odio, dolore nemo a distinctio quam illum
                                    fugiat! Totam, nulla.
                                </p>
                            </div>
                        </div>
                    </div>
                </main>
                <Footer/>
            </div>
        );
    }
}

export default BlogDetails;