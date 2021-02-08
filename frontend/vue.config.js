//development
module.exports = {
    devServer: {
        open: true,  
        host: 'localhost',
        port: 8080, // 端口号
        proxy: {
            '/api': {
              target: 'http://localhost:8000',
              changeOrigin: true, //允许跨域
            }
          }
    },
    publicPath:'./',
  }