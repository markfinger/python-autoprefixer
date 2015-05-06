var autoprefixer = require('autoprefixer-core');

module.exports = {
  functions: {
    autoprefixer: function(data, cb) {
      try {
        var prefixed = autoprefixer(data.options).process(data.css).css;
      } catch(err) {
        return cb(err);
      }
      cb(null, prefixed);
    }
  }
};
