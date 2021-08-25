import {combineReducers} from 'redux'
import authReducer from "./auth/auth";
import blogReducer from './blog';
import albumReducer from './galerie';


const rootReducers = combineReducers({
    auth : authReducer,
    blog : blogReducer,
    album : albumReducer
})

export default rootReducers
