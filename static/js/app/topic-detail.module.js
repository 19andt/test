'use strict';

var app = angular.module('topicDetail', []);

app.service('topicDetailService', function($http, $resource){
    var url = '/topic/detail/:topic_name'
    return $resource(url, {}, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        },
        post: {
            method: 'post',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});