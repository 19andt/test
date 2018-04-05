'use strict';

var app = angular.module('addComment', []);

app.service('addCommentService', function($resource){
    var url = '/comment/add_comment'
    return $resource(url, {}, {
        post: {
            method: 'post',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});