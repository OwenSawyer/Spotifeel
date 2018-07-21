// if (process.env.NODE_ENV !== 'prod') {
//   var webpack = require('webpack')
//   var WebpackDevServer = require('webpack-dev-server')
//   var config = require('./webpack.dev.config')
//
//   new WebpackDevServer(webpack(config), {
//     publicPath: config.output.publicPath,
//     hot: true,
//     headers: { "Access-Control-Allow-Origin": "*" },
//     inline: true,
//     historyApiFallback: true
//   }).listen(process.env.PORT || 3000, '0.0.0.0', function (err, result) {
//     if (err) {
//       console.log(err)
//     }
//
//     console.log('Listening at 0.0.0.0:3000')
//   })
// }
// else{
//
// }
//
