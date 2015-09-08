(function() {
    'use strict';
    angular.module('app', ['controllers'])
    .config(function($locationProvider) {
            $locationProvider.html5Mode(true);
        });
})();
