//development
module.exports = {
    devServer: {
        host: 'localhost',
        port: 8000, // 端口号
        proxy: {
            '/api': {
              target: 'http://39.97.127.205:8000',
              changeOrigin: true, //允许跨域
            }
          }
    },
    publicPath:'./'
  }