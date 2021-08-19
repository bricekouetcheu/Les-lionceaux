import React, { Component } from 'react';



//Components
import Header from '../../components/header/Header'
import Sidebar from '../../components/sidebar/Sidebar'
import {Footer} from '../../components/footer/Footer'

class AjoutsActivite extends Component {
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
                            <h2 class="second-title mb-4">Ajout d'activité</h2>
                            <div class="activite__form">
                                <form class="form-activite form-row">
                                    <div class="col-md-12 mb-4">
                                        <label for="date">Date</label>
                                        <input type="date" id="date" />
                                    </div>
                                    <div class="col-md-6 mb-4">
                                        <label for="heure-1">Debut</label>
                                        <input type="time" id="heure-1"/>
                                    </div>
                                    <div class="col-md-6 mb-4">
                                        <label for="heure-2">Fin</label>
                                        <input type="time" id="heure-2" />
                                    </div>
                                    <div class="col-md-12 mb-4">
                                        <label for="enfant">Groupe</label>
                                        <select id="enfant">
                                            <option value="0">Chosir le groupe</option>
                                            <option value="1">petit</option>
                                            <option value="2">grand</option>
                                        </select>
                                    </div>
                                    <div class="col-md-12 mb-4">
                                        <label for="enfant">Art</label>
                                        <select id="enfant">
                                            <option value="0">Chant</option>
                                            <option value="1">Desin</option>
                                            <option value="2">Danse</option>
                                        </select>
                                    </div>
                                    <div class="col-md-12 mb-4">
                                        <label for="enfant">Lecture</label>
                                        <select id="enfant">
                                            <option value="0">Pichou</option>
                                            <option value="1">Choupi</option>
                                            <option value="2">Dingo</option>

                                        </select>
                                    </div>

                                    <div class="col-md-12 mt-5 text-center">
                                        <button type="button" class="btn-orange">Valider</button>
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

export default AjoutsActivite;