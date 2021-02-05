import service from './httpAPI';
import md5 from 'js-md5'

export function login(postParams){
    return service.request({
        method:'post',
        url:'/login',
        data:{
            email:postParams.email,
            psw:md5(postParams.psw)
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
            psw:md5(postParams.psw),
            captcha:postParams.captcha
        }
    })
}
export function updata(postParams){
    return service.request({
        method:'post',
        url:'/updatapsw',
        data:{
            name:postParams.name,
            oldepsw:postParams.psw_md5,
            psw:postParams.psw_md5
        }
    })
}