import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/";


const login = (username, password) => {
    return axios
        .post(API_URL + "login", {
            username,
            password,
        })
        .then((response) => {
            if (response.data.token) {
                localStorage.setItem("user", JSON.stringify(response.data));
            }

            return response.data;
        });
};

const logout = () => {
    localStorage.removeItem("user");
};


const mylog = {
    login,
    logout
}


export default mylog;