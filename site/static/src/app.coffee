"user strict";

# стили
require('./css/index.less')
require('font-awesome/less/font-awesome.less')

# изображения


require('jquery')
require('angular')
require('bootbox')
require('ngbootbox')
require('bootstrap-notify')
require('../djng/js/django-angular.js')
require('../djng/css/styles.css')

angular.module 'kuzya', [
        require('angular-resource'),
        require('angular-cookies'),
        require('angular-touch'),
        'ngBootbox',
        require('angular-ui-bootstrap'),
        'djng.forms'
    ]
    .config ['$httpProvider', '$cookiesProvider', '$ngBootboxConfigProvider',
    ($httpProvider, $cookiesProvider, $ngBootboxConfigProvider)->
        $httpProvider.defaults.xsrfCookieName = 'csrftoken'
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
        $cookiesProvider.defaults.path = '/'
        $ngBootboxConfigProvider.setDefaultLocale('ru');
        return
    ]
    .run ($rootScope)->
        
        return