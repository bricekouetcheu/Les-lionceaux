import React ,{Component} from 'react'

import {Switch,Route} from 'react-router-dom'


//Pages
import Home from './pages/home/Home'
import Agenda from './pages/agenda/Agenda'
import AjoutsAgenda from './pages/agenda/Ajouts'
import VueAgenda from './pages/agenda/VueAgenda'
import Galerie from './pages/galerie/Galerie'
import Blog from './pages/blog/Blog'
import BlogDetails from './pages/blog/Details'
import Activites from './pages/activites/Activites'
import AjoutsActivite from './pages/activites/Ajouts'
import Contacts from './pages/contacts/Contacts'
import Login from './pages/login/Login'
import Address from './pages/address/Address'
import Horaires from './pages/horaires/Horaires'
import Albums from './pages/albums/Albums'



class App extends Component {

  render(){
      return (
        <Switch>
          <Route path="/" component={Home} exact />
          <Route path="/login" component={Login} exact />
          <Route path="/agenda" component={Agenda} exact />
          <Route path="/add-agenda" component={AjoutsAgenda} exact />
          <Route path="/vue-agenda" component={VueAgenda} exact />
          <Route path="/galerie" component={Galerie} exact />
          <Route path="/blog" component={Blog} exact />
          <Route path="/blog/:slug" component={BlogDetails} exact />
          <Route path="/activity" component={Activites} exact />
          <Route path="/add-activity" component={AjoutsActivite} exact />
          <Route path="/contacts" component={Contacts} exact />
          <Route path="/address" component={Address} exact />
          <Route path="/horaires" component={Horaires} exact />
          <Route path="/albums" component={Albums} exact />
        </Switch>
    );

  }
  
}

export default App;
