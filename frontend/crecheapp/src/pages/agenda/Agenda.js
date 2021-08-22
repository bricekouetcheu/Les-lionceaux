import React, { Component } from 'react';
import {Link} from 'react-router-dom'


//Components
import Header from '../../components/header/Header'
import Sidebar from '../../components/sidebar/Sidebar'
import {Footer} from '../../components/footer/Footer'

class Agenda extends Component {
    render() {
        return (
            <div className="body-home">
                {/* Header */}
                <Header title="Crèche les lionceaux" />

                <main className="main">
                    <Sidebar/>
                    <div class="main__content">
                    {/*Agenda */}
                        <div class="agenda">
                            <div class="activite__title">
                                <h2 class="second-title mb-4">Agenda</h2>
                                <Link to="/add-agenda"><button type="button"
                                        class="btn-default btn-green">Ajouter</button>
                                </Link>
                            </div>
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
                            <div class="agenda__item">
                                <div class="agenda__item--date">
                                    <div class="day flex-center">
                                        <p>02</p>
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
                            <div class="agenda__item">
                                <div class="agenda__item--date">
                                    <div class="day flex-center">
                                        <p>03</p>
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
                            <div class="agenda__item">
                                <div class="agenda__item--date">
                                    <div class="day flex-center">
                                        <p>04</p>
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
                            <div class="agenda__item">
                                <div class="agenda__item--date">
                                    <div class="day flex-center">
                                        <p>05</p>
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
                        </div>
                    </div>
                </main>
                <Footer/>
            </div>
        );
    }
}

export default Agenda;