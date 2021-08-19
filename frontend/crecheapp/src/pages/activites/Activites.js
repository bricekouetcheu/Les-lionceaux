import React, { Component } from 'react';
import {Link} from 'react-router-dom'


//Components
import Header from '../../components/header/Header'
import Sidebar from '../../components/sidebar/Sidebar'
import {Footer} from '../../components/footer/Footer'

class Activites extends Component {
    render() {
        return (
            <div className="body-home">
                {/* Header */}
                <Header title="Crèche les lionceaux" />
                <main className="main">
                    <Sidebar/>
                    <div class="main__content">
                    {/* <!-- activité --> */}
                    <div class="activite">
                        <div class="activite__title">
                            <h2 class="second-title mb-4">Activités</h2>
                            <Link to="/add-activity"><button type="button"
                                    class="btn-default btn-green">Ajouter</button></Link>
                        </div>
                        <div class="row">
                            <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                                <div class="card-activite">
                                    <div class="card-activite__title">
                                        <span>Activité du 19/07/2021</span>
                                    </div>
                                    <div class="card-activite__content">
                                        <ul>
                                            <li>
                                                <img src="images/icon/check.svg" alt="icone" />
                                                <span>Lecture: Pichou</span>
                                            </li>
                                            <li>
                                                <img src="images/icon/check.svg" alt="icone" />
                                                <span>Art: Danse</span>
                                            </li>

                                        </ul>
                                        <p><strong>Groupe: </strong> petit</p>

                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                                <div class="card-activite">
                                    <div class="card-activite__title">
                                        <span>Activité du 19/07/2021</span>
                                    </div>
                                    <div class="card-activite__content">
                                        <ul>
                                            <li>
                                                <img src="images/icon/check.svg" alt="icone" />
                                                <span>Art: Chant</span>
                                            </li>

                                        </ul>
                                        <p><strong>Groupe: </strong> Grand</p>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
                </main>
                <Footer />                
            </div>
        );
    }
}

export default Activites;