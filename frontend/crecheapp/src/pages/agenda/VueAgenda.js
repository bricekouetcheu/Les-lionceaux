import React, { Component } from 'react';
import {Link} from 'react-router-dom'


//Components
import Header from '../../components/header/Header'
import Sidebar from '../../components/sidebar/Sidebar'
import {Footer} from '../../components/footer/Footer'

class VueAgenda extends Component {
    render() {
        return (
            <div className="body-main">
                {/* Header */}
                <Header title="Crèche les lionceaux" />
                <main className="main">
                    <Sidebar />
                    <div className="main__content">
                        
                        <div class="agenda">
                            <h2 class="second-title mb-4">Aperçue agenda</h2>
                            <ul class="breadcrumbs mb-5">
                                <li>
                                    <Link to="/agenda">Agenda</Link>
                                </li>
                                <li>
                                    <Link to="/add-agenda">Ajout</Link>
                                </li>
                                <li>
                                    <Link to="vue-agenda">Aperçue</Link>
                                </li>
                            </ul>
                            <div class="agenda__item">
                                <div class="agenda__item--date">
                                    <div class="day flex-center">
                                        <p>01</p>
                                    </div>
                                    <p>Avril 2021</p>
                                </div>
                                <div class="agenda__item--content">
                                    <p>
                                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Facere,
                                        quas ipsum! Animi veritatis deserunt reiciendis nesciunt ut ipsam vero
                                        omnis laborum totam consequuntur dolores, eius esse maxime possimus ratione error.
                                    </p>
                                </div>
                            </div>
                            <div>
                                <a href="#">
                                    <button type="button" class="btn-dafult btn-green" data-toggle="modal"
                                        data-target="#exampleModalCenter">
                                        Modifier
                                    </button>
                                </a>
                                <button type="button" class="btn-dafult btn-orange">Valiter</button>
                            </div>
                        </div>
                    </div>

                </main>
                <Footer/>
            </div>
        );
    }
}

export default VueAgenda;