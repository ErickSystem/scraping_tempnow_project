import React, { Component } from 'react';
import { Link }             from 'react-router-dom';
import classNames           from 'classnames';

// Icons
import CloseIcon         from 'mdi-react/CloseIcon';
import BriefcaseIcon     from 'mdi-react/BriefcaseIcon';


export default class Header extends Component {

	constructor(props) {
		super(props);

		this.state = {
			flag: false,
			logo: '',
			openMenu: true,
			storeName: ''
		};
	}

	render() {
		return (
			<div className={classNames('nav', { 'opened': this.props.open })}>

				<div>
					<img className="logo" src="iframe-logo.png" alt="logo" />

					<CloseIcon className="close-menu pointer" onClick={ this.props.close }/>

					<nav>
						<ul>
							<li>
								<Link to="WfHours" onClick={ this.toggleMenu }><BriefcaseIcon className="icon-item"/>Wf Hours</Link>
							</li>						
							<li>
								<Link to="WfDays" onClick={ this.toggleMenu }><BriefcaseIcon className="icon-item"/>Wf Days</Link>
							</li>
						</ul>
		
					</nav>
				</div>
				<em>Versão 1.0</em>
			</div>
		);
	}
};
