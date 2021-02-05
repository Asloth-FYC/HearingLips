import service from './httpAPI';
import md5 from 'js-md5'

export function apiAdminMail(params){
    return service.request({
        method:'post',
        url:'/captcha',
        data:{
            email: params.email
        }
    })
}

export function apiAdminForgotPassword(data){
    return service.request({
        method:'post',
        url:'/forgot',
        data:{
            email: data.email,
            newpsw: md5(data.inputPassword),
            captcha: data.code
        }
    })
}

export function get(){
    return service.request({
        method:'post',
        url:'/get',
    })
}

