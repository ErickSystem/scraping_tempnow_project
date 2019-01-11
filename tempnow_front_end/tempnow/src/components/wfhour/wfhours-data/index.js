import React, { Component } from 'react';
import { Table } from 'react-bootstrap'
import Notifications from 'react-notify-toast'

// Services
import * as request from '../../../service/request';

export default class DataWfHours extends Component {

    constructor(props) {
		super(props);
// an example array of items to be paged

		this.state = {
            wfhours: [],
            filter: [],
            wfhour: '',
            status: '',
            loading: true,
            errorMessage: new Map(),
            APIMessageType: ["error","success","warning"],
            filtered: false,
        }
    };

    componentWillMount(){
        request.listWfhours().then(data => {
                this.setState({wfhours: data.wfhours});
        });
    }

    loadData(){
        return this.state.wfhours.map((wfhour) => {
            return (
                <tr key={wfhour.id}>
                    <td>{wfhour.id}</td>
                    <td>{wfhour.atmospheric_pressure}</td>
                    <td>{wfhour.wind}</td>
                    <td>{wfhour.temp}</td>
                    <td>{wfhour.relative_humidity}</td>
                    <td>{wfhour.last_update}</td>
                    <td>{wfhour.weather}</td>
                    <td>{wfhour.locality_id}</td>
                    <td>{wfhour.date_time}</td>
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
                            <th>pressão atmosférica</th>
                            <th>Velocidade do Vento</th>
                            <th>Temperatura</th>
                            <th>Humidade Relativa</th>
                            <th>Última Atualização</th>
                            <th>Tempo</th>
                            <th>localidade id</th>
                            <th>Data e Hora</th>
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