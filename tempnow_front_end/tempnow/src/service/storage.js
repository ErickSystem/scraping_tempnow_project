export function createDataTempNow(){
	
	if (getData('tempnow') == null) {
		localStorage.setItem('tempnow', '{}');
	}
	fetch('config.json')
	.then(function(response) {
		return response.json();
	})
	.then(function(myJson) {			
		setDataTempNow('API', myJson.api_root);
	}).catch(function(error) {
		setDataTempNow('API', "http://localhost:5000/api");
	});
}

export function getData(itemName){
	return JSON.parse(localStorage.getItem(itemName))
}

export function setDataTempNow(nameItem, objData) {
	const valueStringfied = objData ? JSON.stringify(objData) : undefined;

	if (valueStringfied) {
		localStorage.setItem(nameItem, valueStringfied);	
	}
}

export function clearTemNow(){
	localStorage.setItem('tempnow', '{}');
}

export function clear(){
	localStorage.clear();	
};