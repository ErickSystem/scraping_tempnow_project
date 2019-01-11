import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import $ from 'jquery';
import 'bootstrap';
import 'bootstrap-select';

export default class Select extends Component {
	constructor(props) {
        super(props);

        this.state = {
            
        }
	}

	componentDidMount () {
		const $select = $(ReactDOM.findDOMNode(this))
		
		$select.selectpicker('refresh');
		$select.selectpicker('refresh').trigger('change');
		$select.selectpicker('val', this.props.value);
		$select.selectpicker('render');		
		
		if(this.props.reset)			
			document.getElementsByClassName('bs-deselect-all')[0].onclick = this.props.reset;					

	}
	componentDidUpdate () {
		const $select = $(ReactDOM.findDOMNode(this))
		$select.selectpicker('refresh');
		$select.selectpicker('val', this.props.value);
		$select.selectpicker('render');		
	}
	forceChange(){
		const $select = $(ReactDOM.findDOMNode(this));	
		$select.selectpicker('refresh').trigger('change');				
	}
	getSelectedIndex(){
		const $select = $(ReactDOM.findDOMNode(this));	
		if($select.find(':selected')[0])
			return $select.find(':selected')[0].index;
		else
			return -1;
	}
	render() {		
		const {value, reset, ...props} = this.props;
		return <select className="selectpicker" {...props} />
	}
};
