import React from 'react';

/*import { NavLink } from 'react-router-dom';*/

import Footer from '../../components/footer';
import Header from '../../components/header';
import Navbar from '../../components/navbar'


const Blog_detail = () => {
    return (
        <div><h1> <div class="body-home">
       
        <Header/>
        
    
        <main class="main">
           <Navbar/>
            <div class="main__content">
                
                <div class="blog">
                    <h2 class="second-title mb-4">Blog detail</h2>
                    <div class="blog-img">
                        <img src="images/photo/galerie-2.jpg" alt="image"/>
                    </div>
                    <div class="blog-text">
                        <h3 class="third-title">Titre du blog</h3>
                        <ul>
                            <li><strong>Auteur </strong>: Joel Yepgang</li>
                            <li><strong>Date </strong>: 30/04/2021</li>
                        </ul>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil accusantium velit, 
                            nobis similique, magnam eligendi laudantium tempore aperiam beatae corrupti perferendis, 
                            fugiat vero odio ut amet numquam. Ducimus, totam illo?
                            Dolores ullam delectus fuga dolore ex deserunt non accusantium reiciendis consequuntur 
                            minus nam, quam quidem earum illo? Dolorum libero voluptas cumque harum aut minima consequuntur 
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
</h1></div>
    );
};

export default Blog_detail;