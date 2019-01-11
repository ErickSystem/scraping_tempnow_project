import React, { Component }  from 'react';
import { Col, Row }	from 'react-bootstrap';
import Notifications from 'react-notify-toast'

// Components
import DataWfDays      from '../components/wfday/wfdays-data';

export default class WFDays extends Component {

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
						<DataWfDays 
							onChange={(e) => this.setState({ numStores: e })} 
							showModal={ this.showModal } 
							filter={ this.state.filter } 
							wfday={ this.state.wfhour } 
							status={ this.state.status } 
						/>
					</Col>
				</Row>				
			</div>
	    );
	}
};
