import React from 'react';

/*import { NavLink } from 'react-router-dom';*/


const Login = () => {
    return (
        <div class="body-login flex-center">
        <div class="box-login">
            <div class="box-login__illustration">
               
                <img src="images/children-school.jpg" alt=""/>
            </div>
            <div class="box-login__form">
                <p class="box-logo text-center">
                    <a href="index.html"><img src="images/logo-nan.png" class="logo-site mb-2" alt="logo"/></a>
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
                    <button type="button" class="btn-orange">Connexion</button>
                </form>
                <div class="copyright">
                    <small>&copy; 2021 - Tout Droit Reservé</small>
                </div>
            </div>
        </div>
    </div>
    );
};

export default Login;