//用于测试前后端axios交互的接口

import service from './httpAPI';

export function helloFlask(){
    return service.request({
        method:'get',
        url:'/hello'
    })
}