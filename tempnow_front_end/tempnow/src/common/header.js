import React, { Component } from 'react';
import * as storage         from '../service/storage';

// Icons
import MenuIcon       from 'mdi-react/MenuIcon';
import DotsHorizontal from 'mdi-react/DotsHorizontalIcon';

export default class Header extends Component {

	constructor(props) {
		super(props);
		
		this.state = {
			flag: false,
			logo: '',
			openMenu: false,
			storeName: '',
		}
	}

	componentDidMount() {
		const logo = storage.getData('fx').logo;
		this.setState({ logo: logo });
	};

	toggleOpen = (e) => {
		this.setState({ flag: !this.state.flag });
	}

	render() {
	    return (
			<header className="relative">

				<MenuIcon className="icon-menu pointer" onClick={ this.props.click }/>

				<a href="#/wfhours"><img className="logo" src="iframe-logo.png" alt="logo" /></a>
				
				<DotsHorizontal className="icon-logout" onClick={ this.toggleOpen }/>

			</header>
	    );
	}
};


