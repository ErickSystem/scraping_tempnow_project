import React, { Component } from 'react';
import { Grid }    		    from 'react-bootstrap';
import classNames from 'classnames';
import Notifications from 'react-notify-toast'

import Header             	from '../common/header';
import Nav               	from '../common/nav';
import $ 					from 'jquery';

export default class Layout extends Component {

	constructor(props){
		super(props);

		this.state = {
			openMenu: false,
		}
	};

	toggleMenu = () => {
		this.setState({ openMenu: !this.state.openMenu });
	};

	closeOnClickOutside() {
		$('body').on('click', (e) => {
			let notNavOrChild = !$(e.target).parents('.nav').length && !$(e.target).hasClass('nav');

			if ($('.nav').hasClass('opened') && notNavOrChild) {
				this.setState({ openMenu: !this.state.openMenu });
			}
		});

		return;
	}

	setLanguage = (e) => {
		sessionStorage.removeItem('lang');
		sessionStorage.setItem('lang', 'br');
		window.location.reload();
	}

	render() {
		this.closeOnClickOutside();
		const { children } = this.props
		
		return (
			<Grid className={ classNames("dashboard structure relative", JSON.parse(localStorage.getItem('tempnow')).kind) }>
				<Header click={ this.toggleMenu } lang={ this.setLanguage }/>
				<Nav open={ this.state.openMenu } close={ this.toggleMenu }/>
				<Notifications />
				<div>{ children }</div>
			</Grid>
		);
	}
};
