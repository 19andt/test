'use strict';

var app = angular.module('getReviewsByUser', []);

app.service('getReviewsByUserService', function($http, $resource){
    var url = '/review/get_reviews_by_user/:username'
    return $resource(url, {}, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});