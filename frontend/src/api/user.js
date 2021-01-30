import service from './httpAPI';

export function login(postParams){
    return service.request({
        method:'post',
        url:'/login',
        data:{
            email:postParams.email,
            psw:postParams.psw_md5
        }
    })
}


export function register(postParams){
    return service.request({
        method:'post',
        url:'/regi',
        data:{
            name:postParams.name,
            email:postParams.email,
            psw:postParams.psw_md5
        }
    })
}