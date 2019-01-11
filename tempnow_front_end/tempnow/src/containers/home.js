import React, { Component } from 'react';
import Notifications from 'react-notify-toast'

// Components

export default class Home extends Component {
	render() {
		return (
			<div className="home">
				<Notifications />
			</div>
		);
	}
};
