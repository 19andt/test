'use strict';

var app = angular.module('getReviewsUser', []);

app.service('getReviewsUserService', function($http, $resource){
    var url = '/review/get_reviews_user'
    return $resource(url, {}, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});