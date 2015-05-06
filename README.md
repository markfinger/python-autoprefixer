# python-autoprefixer

Python bindings to autoprefixer

Installation
------------

Install [js-host](https://github.com/markfinger/python-js-host)

```bash
pip install autoprefixer
npm install --save autoprefixer-core
```

Add the following to your `host.config.js`

```javascript
var autoprefixer = require('autoprefixer-core');

module.exports = {
  functions: {
    // ...
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
```


Usage
-----

```python
from autoprefixer.compiler import autoprefixer

prefixed_css = autoprefixer('body { color: red; }')

prefixed_css = autoprefixer('/path/to/file.css', options={'browsers': ['> 1%', 'IE 7']})

prefixed_css = autoprefixer('/path/to/file.css', is_file=True)

prefixed_css = autoprefixer('/path/to/file.css', is_file=True, options={'browsers': ['> 1%', 'IE 7']})
```
