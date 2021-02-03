import axios from 'axios'


//创建axios实例
const service = axios.create({
    baseURL: '/api',    
    timeout: 1000000,
});

//请求拦截器
service.interceptors.request.use(
    function(config){
        if(localStorage.getItem('Authorization')){
            config.headers.token = localStorage.getItem('Authorization');
        }
        return config;
    },
    function(error){
        return Promise.reject(error);
    }
);

//响应拦截器
service.interceptors.response.use(
    function(response){
        console.log(response);
        return response;
    },
    //服务器没有响应
    function(error){
        return Promise.reject(error);
    }
);

//对外暴露接口
export default service;