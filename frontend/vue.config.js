const path = require('path');

module.exports = {
  publicPath: '/',
  chainWebpack: config => {
    config.module.rules.delete('eslint');
  },
  css: {},
  configureWebpack: {
    resolve: {
      extensions: ['.js', '.vue', '.json'],
      alias: {
        '@': path.resolve('src/'),
        'fonts': path.resolve('src/assets/fonts'),
        'vue$': 'vue/dist/vue.esm.js'
      }
    },
    module: {
      rules: [
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],
        },
      ]
    },
    plugins: []
  },
  devServer: {
    host: '0.0.0.0',
    hot: true,
    disableHostCheck: true,
    watchOptions: {
      poll: true
    }
  },
  pluginOptions: {}
}