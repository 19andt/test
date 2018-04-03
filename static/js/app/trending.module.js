'use strict';

var app = angular.module('trending', []);

app.service('trendingService', function($resource){
    var url = '/trending_list'
    return $resource(url, {}, {
        get: {
            method: 'get',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});