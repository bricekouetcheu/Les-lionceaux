import {combineReducers} from 'redux'
import authReducer from "./auth/auth";
import blogReducer from './blog';


const rootReducers = combineReducers({
    auth : authReducer,
    blog : blogReducer
})

export default rootReducers
