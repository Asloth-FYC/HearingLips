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
export function updatePsw(postParams){
    return service.request({
        method:'post',
        url:'/updatePsw',
        data:{
            oldPsw:md5(postParams.inputOpassword),
            psw:md5(postParams.inputpassword),
        }
    })
}