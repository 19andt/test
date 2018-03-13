'use strict';

var app = angular.module('getTopic', []);

app.service('getTopicService', function($http, $resource){
    var url = '/topic/get_topic/:topic_name'
    return $resource(url, {}, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});