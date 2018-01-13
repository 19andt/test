'use strict';

var app = angular.module('searchTopic', []);

app.service('searchTopicService', function($http, $resource){
    var url = '/topic/search_topic'
    return $resource(url, {}, {
        post: {
            method: 'POST',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});