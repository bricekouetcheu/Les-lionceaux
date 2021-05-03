import React from 'react';

import { Route, Switch } from "react-router-dom";


import Home from "./pages/index";
import Adresse from './pages/adresse';
import Apropos from './pages/apropos';
import Contact from './pages/contact';
import Horaire from './pages/horaire';
import Galerie from  './pages/galerie';
import Album from  './pages/album';
/*import Projet_pedagogie from './pages/projet_pedagogie'; */
import Login from './components/login';




const BaseRouter = () => {
    return (
        <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/login" component={Login} />
            <Route exact path="/adresse" component={Adresse} />
            <Route exact path="/propos" component={Apropos} />
            <Route exact path="/contact" component={Contact} />
            <Route exact path="/horaire" component={Horaire} />
            <Route exact path="/galerie" component={Galerie} />
            <Route exact path="/album" component={Album} />
        </Switch>
    );
};

export default BaseRouter;