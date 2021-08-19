import React, { Component } from 'react';
import {Link } from 'react-router-dom'



//Components
import Header from '../../components/header/Header'
import Sidebar from '../../components/sidebar/Sidebar'
import {Footer} from '../../components/footer/Footer'

//Images
import ChildrenSchool from "../../assets/images/children-school.jpg"
import Logo from "../../assets/images/logo-nan.png"



class Login extends Component {
    render() {
        return (
            <div className="body-login flex-center">
                <div class="box-login">
                    <div class="box-login__illustration">
                        {/* <iframe src="https://youtu.be/NIk1-ck4c6Q" frameborder="0"></iframe> */}
                        <img src={ChildrenSchool} alt="" />
                    </div>
                    <div class="box-login__form">
                        <p class="box-logo text-center">
                            <a href="index.html"><img src={Logo} className="logo-site mb-2" alt="logo" /></a>
                        </p>
                        <h1 class="text-center mb-5">Crèche les lionceaux</h1>
                        <div class="mb-3">
                            <h2>Login <span class="dot"></span></h2>
                            <p>
                                Bienvenu(e) sur Cretch de la creme <br/>
                                Authentifiez-vous :)
                            </p>
                        </div>
                        <form class="form-login">
                            <label for="identifiant">Identifiant</label>
                            <input type="text" id="identifiant" placeholder="AZERTY5112"/>
                            <label for="password">Mot de passe</label>
                            <input type="password" id="password" placeholder=".........."/>
                            <a href="index.html">
                                <button type="button" class="btn-orange">Connexion</button>
                            </a>
                            <Link to="/">
                                <button type="button" class="ml-2 btn-orange">Acceuil</button>
                            </Link>
                        </form>
                        <div class="copyright">
                            <small>&copy; 2021 - Tout Droit Reservé</small>
                        </div>
                    </div>
                </div>

                
            </div>
        );
    }
}

export default Login;