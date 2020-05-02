import axios from 'axios';

axios.defaults.baseURL = `/api/`;

axios.defaults.headers.common['Content-Type'] = 'application/json';
axios.defaults.headers.common['Access-Control-Allow-Credentials'] = 'true';
axios.defaults.headers.common['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Set-Cookie, *';
axios.defaults.headers.common['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,PATCH';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

axios.interceptors.request.use(request => {
    if (request.params === null || typeof request.params !== 'object') {
        request.params = {};
    }
    return request;
});

export default axios;