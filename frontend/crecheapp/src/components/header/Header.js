import React, {Component} from 'react'
import {Link} from 'react-router-dom'




//Images
import LogoNan from '../../assets/images/logo-nan.png'
import Menu from '../../assets/images/icon/menu.svg'

class Header extends Component {
    constructor(props){
        super(props);
    }
    render(){
        const {title} = this.props
        return (
            (
        
                <header className="header">
                    <div className="header__logo">
                        <img src={LogoNan} alt="logo site" />
                    </div>
                    <div class="header__title">
                        <h1>{title}</h1>
                    </div>
                    <div class="header__btn">
                        <Link to="/login"><button type="button"
                                className="btn-orange border-orange-header">Connexion</button>
                        </Link>
                    </div>
                    <button type="button" className="btn-menu">
                        <img src={Menu} alt="" />
                    </button>
                </header>
            )
        )
    }
} 

export default Header
    
