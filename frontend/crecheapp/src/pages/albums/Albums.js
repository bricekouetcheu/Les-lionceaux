import React, { Component } from 'react';
import {Link} from 'react-router-dom'


//Components
import Header from '../../components/header/Header'
import Sidebar from '../../components/sidebar/Sidebar'
import {Footer} from '../../components/footer/Footer'

//Images
import C1 from '../../assets/images/c1.jpeg'

class Albums extends Component {
    render() {
        return (
            <div className="body-home">
                {/* Header */}
                <Header title="Crèche les lionceaux" />
                <main className="main">
                    <Sidebar />
                    <div className="main__content">
                    {/* <!-- galerie --> */}
                    <div className="box-galerie">
                        <div className="activite__title">
                            <h2 className="second-title mb-4">Album</h2>
                            <Link to="#"><button type="button"
                                    className="btn-default btn-green">Ajouter</button></Link>
                        </div>
                        <div className="row">
                            <div className="col-lg-3 col-md-4 col-sm-4 col-6">
                                <Link to="/galerie">
                                    <div className="card-album">
                                        <div className="card-album__img">
                                            <img src={C1} alt="images" />
                                        </div>
                                        <div className="card-album__title">
                                            <h4 className="four-title">Titre de l'album</h4>
                                        </div>
                                    </div>
                                </Link>
                            </div>
                            <div className="col-lg-3 col-md-4 col-sm-4 col-6">
                                <Link to="/galerie">
                                    <div className="card-album">
                                        <div className="card-album__img">
                                            <img src={C1} alt="images" />
                                        </div>
                                        <div className="card-album__title">
                                            <h4 className="four-title">Titre de l'album</h4>
                                        </div>
                                    </div>
                                </Link>
                            </div>
                            <div className="col-lg-3 col-md-4 col-sm-4 col-6">
                                <Link to="/galerie">
                                    <div className="card-album">
                                        <div className="card-album__img">
                                            <img src={C1} alt="images" />
                                        </div>
                                        <div className="card-album__title">
                                            <h4 className="four-title">Titre de l'album</h4>
                                        </div>
                                    </div>
                                </Link>
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

export default Albums;