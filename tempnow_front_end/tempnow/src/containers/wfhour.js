import React, { Component }  from 'react';
import { Col, Row }	from 'react-bootstrap';
import Notifications from 'react-notify-toast'

// Components
import DataWfHours      from '../components/wfhour/wfhours-data';

export default class WfHours extends Component {

	constructor(props) {
		super(props)
		this.state = {
			filter: {},
		}
	}

	render() {
	    return (
	    	<div className="wfhours">
				<Notifications />
				<Row>
					<Col sm={ 12 }>
						<DataWfHours 
							onChange={(e) => this.setState({ numStores: e })} 
							showModal={ this.showModal } 
							filter={ this.state.filter } 
							wfhour={ this.state.wfhour } 
							status={ this.state.status } 
						/>
					</Col>
				</Row>				
			</div>
	    );
	}
};
