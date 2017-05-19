'use strict';
// ## bootstrap-webpack Configuration

var loader = require('extract-text-webpack-plugin').extract({ 
  fallback: 'style-loader', use: [
        {
            loader: "css-loader", // translates CSS into CommonJS
            options: {
                minimize: true
            }
        },
        {
            loader: "less-loader" // compiles Less to CSS
        }
    ]
})
if (process.env.NODE_ENV === 'prod') {
  var styleLoader = loader.map( chunk => {
    const path = chunk.loader

    if (chunk.options) {
      const options = JSON.stringify(chunk.options)
      return `${path}?${options}`
    }

    return path
  }).join('!')
} else {
  var styleLoader = null
}

module.exports = {
  // ### Scripts
  // Any scripts here set to false will never
  // make it to the client, it's not packaged
  // by webpack.
  styleLoader: styleLoader,
  scripts: {
    'transition': false,
    'alert': false,
    'button': false,
    'carousel': false,
    'collapse': false,
    'dropdown': false,
    'modal': true,
    'tooltip': false,
    'popover': false,
    'scrollspy': false,
    'tab': false,
    'affix': false
  },
  // ### Styles
  // Enable or disable certain less components and thus remove
  // the css for them from the build.
  styles: {
    "mixins": true,

    "normalize": true,
    "print": true,

    "scaffolding": true,
    "type": true,
    "code": true,
    "grid": false,
    "tables": true,
    "forms": true,
    "buttons": true,

    "component-animations": true,
    "glyphicons": false,
    "dropdowns": true,
    "button-groups": true,
    "input-groups": true,
    "navs": true,
    "navbar": true,
    "breadcrumbs": true,
    "pagination": true,
    "pager": false,
    "labels": true,
    "badges": true,
    "jumbotron": false,
    "thumbnails": false,
    "alerts": true,
    "progress-bars": false,
    "media": false,
    "list-group": true,
    "panels": false,
    "wells": false,
    "close": true,

    "modals": true,
    "tooltip": true,
    "popovers": false,
    "carousel": true,

    "utilities": true,
    "responsive-utilities": false
  }
};