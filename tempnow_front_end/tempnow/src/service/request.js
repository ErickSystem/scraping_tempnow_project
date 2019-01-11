import axios from 'axios'
import * as storage   from './storage';

axios.defaults.timeout = 60000;

export function urlBase(){
    var urlBase = '';
    
    urlBase = storage.getData('API');
    console.log(urlBase)
    
    return urlBase;    
}

//WF HOURS
export function listWfhours(){
    const options = { headers: { 'content-type': 'application/json' } }
    return axios.get(urlBase()+'/wfhours/'+24, options).then(response => {
            if(response.data.success){ 
                return response.data;	    	
            } else{
                return response;
            }
        });
}

//WF DAYS
export function listWfdays(){

    return axios.get(urlBase()+'/wfdays/'+24).then(response => {
            if(response.data.success){ 
                return response.data;	    	
            } else{
                return response;
            }
        });
}