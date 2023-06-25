const path = require('path');

module.exports = {
  mode: 'development',
  entry: {
    'play_game': './server/static/compiled/play_game/App.js',
    'new_game': './server/static/compiled/new_game/NewGame.js'
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, './server/static/dist'),
  },
};