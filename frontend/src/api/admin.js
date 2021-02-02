import service from './httpAPI';

export function apiAdminForgetMail(params){
    return service.request({
        method:'post',
        url:'/admin/forget/mail',
        data:{
            username: params.username,
            email: params.email
        }
    })
}

export function apiAdminForgetPassword(data){
    return service.request({
        method:'post',
        url:'/admin/forget/password',
        data:{
            username: data.username,
            email: data.email
        }
    })
}
