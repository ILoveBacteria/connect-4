const path = require('path');

module.exports = {
  mode: 'development',
  entry: './server/static/compiled/App.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, './server/static/dist'),
  },
};