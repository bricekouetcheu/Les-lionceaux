import React, { Component } from 'react';

import {Link} from 'react-router-dom'



//Components
import Header from '../../components/header/Header'
import Sidebar from '../../components/sidebar/Sidebar'
import {Footer} from '../../components/footer/Footer'

class AjoutsAgenda extends Component {
    render() {
        return (
            <div className="body-home">
                {/* Header */}
                <Header title="Crèche les lionceaux" />
                <main className="main">
                    <Sidebar />
                    <div class="main__content">
                    {/* <!-- Agenda --> */}
                    <div class="agenda">
                        <h2 class="second-title mb-4">Ajout agenda</h2>
                        <ul class="breadcrumbs">
                            <li>
                                <Link to="/agenda">Agenda</Link>
                            </li>
                            <li>
                                <Link to="/add-agenda">Ajout</Link>
                            </li>
                        </ul>
                        <div class="activite__form">
                            <form class="contact__form">
                                <div class="mb-4">
                                    <label for="date">Date</label>
                                    <input type="date" id="date" />
                                </div>
                                <div>
                                    <label for="agenda">Agenda</label>
                                    <textarea name="" id="agenda"></textarea>
                                </div>
                                <div class="mt-5 text-center">
                                    <Link to="/vue-agenda">
                                        <button type="button" class="btn-orange">Aperçue</button>
                                    </Link>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

                </main>
                <Footer/>
            </div>
        );
    }
}

export default AjoutsAgenda;