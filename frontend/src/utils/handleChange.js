import { searchCEP } from "./request/apiRequest";

export function handleChangeCep(component, object, objectKey, event, callback) {
    const cep = event.target.value
    let currentObject = object
    if (cep.length === 8) {
        searchCEP(cep).then((r) => {
            if (r.error) {
                throw r.error
            }
            currentObject.bairro = r.district
            currentObject.logradouro = r.street
            currentObject.codibge = r.ibge
            currentObject.cidade = r.city
            currentObject.cep = cep
            console.log(currentObject)
            component.setState(currentObject, callback)
        }).catch((error) => {
            currentObject.cep = cep
            component.setState({
                alertMessage: 'CEP não encontrado',
                alertType: 'error',
                showAlert: true,
                [objectKey]: currentObject
            }, callback)
        })  
    } else {
        currentObject.cep = cep
        component.setState(currentObject, callback)
    }
}

export function handleChangeImage(component, object, hexString, fieldName, callback) {
    object[fieldName] = hexString
    component.setState(object, callback)
}

export function handleChangeText(object, keyPath, value, callback) {
    // Separa o keyPath em uma array de chaves
    const keys = keyPath.split(".");
  
    // Navega pelo objeto até a chave final
    let currentObject = object;
    for (let i = 0; i < keys.length - 1; i++) {
        if (!currentObject.hasOwnProperty(keys[i])) {
            currentObject[keys[i]] = {};
        }
        currentObject = currentObject[keys[i]];
    }
  
    // Atualiza o valor da chave final
    currentObject[keys[keys.length - 1]] = value;

    callback()
}