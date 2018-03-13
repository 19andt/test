'use strict';

var app = angular.module('updateTopic', []);

app.service('updateTopicService', function($http, $resource){
    var url = '/topic/update_topic'
    return $resource(url, {}, {
        post: {
            method: 'post',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});