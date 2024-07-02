import axios from 'axios';
import { showUnauthorizedModal } from '../layout';

export const defaultRequest = async (config, form) => {
    
    var url = new URL('http://localhost:8000/' + config.endpoint)

    var data = {}

    const token = localStorage.getItem('userToken')

    var headers = {
        'Content-Type': 'application/json'
    }

    if (token){
        headers['Authorization'] = 'Bearer ' + token
    }

    if (config.method === 'get' || config.method === 'delete') {
        url.search = new URLSearchParams(form)
    } 
    else if (config.method === 'post' || config.method === 'put') {
        data = form
    }

    var funcResponse = {}

    try {
        const response = await axios({
            headers: headers,
            method: config.method.toLowerCase(),
            url: url.toString(),
            data: data
        })

        funcResponse = {
            status: true,
            data: response.data
        }
    } catch (error) {
        if (error.response.status === 401) {
            localStorage.removeItem('userToken')
            showUnauthorizedModal()
        } else {
            funcResponse = {
                status: false,
                data: error.response.data
            }
        }
    }    

    return funcResponse   
}

export const getCityOptionsRequest = (component, uf) => {
    let config = {
        method: 'get',
        endpoint: 'list/city'
    }
    let form = {
        uf: uf 
    }
    return defaultRequest(config, form)
}

export const optionsRequest = (component, optionList) => {
    let config = {
        method: 'get',
        endpoint: 'list/options'
    }
    let form = {
        optionList: JSON.stringify(optionList)
    }
    defaultRequest(config, form).then((r) => {
        if (r.status) {
            var newState = {}
            for ( let key in r.data ) {
                if (!['status', 'message'].includes(key)) {
                    if (r.data.hasOwnProperty(key)) {
                        const camelCase = key.replace(/_([a-z])/g, (g) => g[1].toUpperCase())
                        newState[camelCase] = r.data[key]
                    }
                }
            }
            newState['isLoadingOptions'] = false

            component.setState(prevState => ({ 
                ...prevState, ...newState 
            }))
        }
    })
}