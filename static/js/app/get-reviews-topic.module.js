'use strict';

var app = angular.module('getReviewsTopic', []);

app.service('getReviewsTopicService', function($http, $resource){
    var url = '/review/get_reviews_topic/:topic_name'
    return $resource(url, { topic_name: '@id' }, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});