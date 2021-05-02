import React from 'react';

import { Route, Switch } from "react-router-dom";


import Home from "./pages/index";
import Adresse from './pages/adresse';
import Apropos from './pages/apropos';
import Contact from './pages/contact';
import Horaire from './pages/horaire';
import Projet_pedagogie from './pages/projet_pedagogie';
import Login from './components/login';
import Blog_detail from './pages/blog/blog_detail';
import Blog from "./pages/blog/blog";




const BaseRouter = () => {
    return (
        <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/login" component={Login} />
            <Route exact path="/adresse" component={Adresse} />
            <Route exact path="/propos" component={Apropos} />
            <Route exact path="/contact" component={Contact} />
            <Route exact path="/horaire" component={Horaire} />
            <Route exact path="/projet" component={Projet_pedagogie} />
            <Route exact path="/blog" component={Blog} />
            <Route exact path="/blog-detail" component={Blog_detail} />
        </Switch>
    );
};

export default BaseRouter;