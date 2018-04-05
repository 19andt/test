'use strict';

var app = angular.module('getObserverCount', []);

app.service('getObserverCountService', function($http, $resource){
    var url = '/subscription/get_observer_count'
    return $resource(url, {}, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});