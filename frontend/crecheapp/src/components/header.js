import React from 'react';



import { NavLink } from 'react-router-dom';



const Header = () => {

    

    return (

        <header class="header">
            <div class="header__logo">
                <img src="images/logo-nan.png" alt="logo site" />
            </div>
            <div class="header__title">
                <h1>Crèche les lionceaux</h1>
            </div>
            
                <div class="header__btn">
                    <NavLink to="/login"><button type="button" class="btn-orange border-orange-header">Connexion</button></NavLink>
                </div>
            
            <button type="button" class="btn-menu">
                <img src="images/icon/menu.svg" alt="" />
            </button>
        </header>

    );
};