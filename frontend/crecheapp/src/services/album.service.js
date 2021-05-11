import axios from "axios";

const API_URL = "https://127.0.0.1:8000/api/";


const getAllAlbum = () => {

    return axios
        .get(API_URL + "album/", {})
};


const getAlbum = slug => {
    console.log("myslud", slug);
    return axios.get(API_URL + `galerie-by-album/${slug}`, {})
};


const myAlbum = {
    getAllAlbum,
    getAlbum
}


export default myAlbum;
