import { combineReducers } from 'redux'
import authReducer from "./auth/auth";
import blogReducer from './blog';
import albumReducer from './galerie';



const rootReducers = combineReducers({
    auth : authReducer,
    blog : blogReducer,
    album : albumReducer

import agendaReducer from './agenda'

const rootReducers = combineReducers({
    auth: authReducer,
    blog: blogReducer,
    album: albumReducer,
    agenda: agendaReducer

})

export default rootReducers
