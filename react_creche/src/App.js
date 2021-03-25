import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Blog from "./pages/Blog";
import Galerie from "./pages/Galerie";
import Home from "./pages/Home";
import Projet from "./pages/Projet";
import Contact from "./pages/Contact";

const App = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/Blog" exact component={Blog} />
        <Route path="/Galerie" exact component={Galerie} />
        <Route path="/Projet" exact component={Projet} />
        <Route path="/Contact" exact component={Contact} />
      </Switch>
    </BrowserRouter>
  );
};

export default App;
