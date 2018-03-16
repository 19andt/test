'use strict';

var app = angular.module('addTopic', []);

app.service('addTopicService', function($resource){
    var url = '/topic/add_topic'
    return $resource(url, {}, {
        post: {
            method: 'post',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});