import axios from "axios";

const API_URL = "https://127.0.0.1:8000/api/";


const getAllBlog = () => {

    return axios
        .get(API_URL + "blog/", {})
};


const getBlog = id => {
    console.log("myslud", id);
    return axios
        .get(API_URL + `blog/${id}`, {})
};


const myBlog = {
    getAllBlog,
    getBlog
}


export default myBlog;