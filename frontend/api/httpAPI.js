import axios from 'axios'


//创建axios实例
const instance = axios.create({
    //baseURL: '',    
    timeout: 5000,
});

//请求拦截器
instance.interceptors.request.use(
    function(error){
        return Promise.reject(error);
    }
);

//响应拦截器
instance.interceptors.response.use(
    //服务器没有响应
    function(error){
        return Promise.reject(error);
    }
)