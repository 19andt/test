'use strict';

var app = angular.module('updateRating', []);

app.service('updateRatingService', function($resource){
    var url = '/rating/update_rating'
    return $resource(url, {}, {
        post: {
            method: 'post',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});