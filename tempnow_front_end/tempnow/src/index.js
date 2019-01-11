// Imports
import React                from 'react';
import ReactDOM             from 'react-dom';
import 'jquery';
import * as storage         from './service/storage';
import { HashRouter, Route, Switch } from 'react-router-dom';

// CSS
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-select/dist/css/bootstrap-select.min.css';
import './assets/style/main.sass';

// Contents
// Main navigation
import Structure      from './containers/structure';
import Wfhours        from './containers/wfhour';
import WfDays		  from './containers/wfdays';

// Create localStorage
storage.createDataTempNow();

const showWfhours = () => {
	return <Structure><Wfhours /></Structure>
}

const showWfdays = () => {
	return <Structure><WfDays /></Structure>
}

ReactDOM.render(
	<HashRouter>
		<div>
			<Route exact path="/" component={ showWfhours } />
			<Switch>
				<Route exact path="/wfhours" component={ showWfhours } />
				<Route exact path="/wfdays" component={ showWfdays } />
			</Switch>
		</div>
	</HashRouter>,
	document.getElementById('root')
);
