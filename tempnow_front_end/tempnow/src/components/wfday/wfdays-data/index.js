import React, { Component } from 'react';
import { Table } from 'react-bootstrap'
import Notifications from 'react-notify-toast'

// Services
import * as request from '../../../service/request';

export default class DataWfDays extends Component {

    constructor(props) {
		super(props);
// an example array of items to be paged

		this.state = {
            wfdays: [],
            filter: [],
            status: '',
            loading: true,
            errorMessage: new Map(),
            APIMessageType: ["error","success","warning"],
            filtered: false,
        }
    };

    componentWillMount(){
        request.listWfdays().then(data => {
                this.setState({wfdays: data.wfdays});
        });
    }

    loadData(){
        return this.state.wfdays.map((wfday) => {
            return (
                <tr key={wfday.id}>
                    <td>{wfday.id}</td>
                    <td>{wfday.precipitation}</td>
                    <td>{wfday.date}</td>
                    <td>{wfday.max}</td>
                    <td>{wfday.min}</td>
                    <td>{wfday.weather}</td>
                    <td>{wfday.locality_id}</td>
                    <td>{wfday.lag}</td>
                </tr>
            )
        })
    }
 
    render() {
        return (
            <div>
                <Notifications options={{zIndex: 10000, top: '50px'}}/>
                <Table responsive>
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>Precipitação</th>
                            <th>Data</th>
                            <th>Máxima</th>
                            <th>Minima</th>
                            <th>Tempo</th>
                            <th>ID Localidade</th>
                            <th>Lag</th>
                        </tr>
                    </thead>
                    <tbody>
                        { this.loadData() }
                    </tbody>
                </Table>
            </div>
        )
    };
       
}