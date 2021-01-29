//development
module.exports = {
    devServer: {
        host: 'localhost',
        port: 8000, // 端口号
        proxy: {
            //项目中请求路径为api的都替换为target
            '/api': {
              target: 'http://localhost:5000',
              changeOrigin: true, //允许跨域
              pathRewrite: {'^/api' : '/'}
            }
          }
    },
    
  }