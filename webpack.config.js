const path = require('path');

module.exports = {
  entry: './src/proto/export.js',
  optimization: {
    minimize: false
  },
  output: {
    path: path.resolve("src/web/js"),
    filename: "service.js",
  }
};