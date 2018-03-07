'use strict';

var app = angular.module('topic', []);

app.component('topic', {
        templateUrl: '/ang/templates/topic.html'
    });

app.controller('topicController', function($rootScope, $scope, $routeParams){
    $scope.topic_name = $routeParams.topic_name
});