import {BASE_URL} from '../../config/urls/base'

//ALBUMS
const albumList = async () => {
    const url = `${BASE_URL}album`
    const options = {
        method : 'GET'
    }
    const response = await fetch(url,options)
    const data = response.json()
    return data
}
const albumGalerie = async (id) => {
    const url = `${BASE_URL}album/${id}/`
    const options = {
        method : 'GET'
    }
    const response = await fetch(url,options)
    const data = response.json()
    return data
}


export {albumList,albumGalerie}