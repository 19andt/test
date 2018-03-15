'use strict';

angular.module('ReviewBag', [
    // External
    'ngResource',
    'ngRoute',
    'ui.bootstrap',
    'ngMaterial',
    'ngMessages',
    'angularMoment',
    'ngSanitize',
    'ui.bootstrap',

    // Internal
    'home',
    'navBar',
    'checkAuthentication',
    'login',
    'logout',
    'addUser',
    'authentication',
    'userAuthentication',
    'getInterest',
    'interest',
    'searchTopic',
    'updateInterest',
    'interestList',
    'addReview',
    'newReview',
    'getReviewsUser',
    'homeReviewList',
    'rbControllers',
    'updateRating',
    'fromNow',
    'topic',
    'topicReviewList',
    'getReviewsTopic',
    'test',
    'getTopic',
    'updateTopic',
    'searchText',
]);

angular.module('ReviewBag').
    config(
        function($locationProvider, $routeProvider, $httpProvider){
            $locationProvider.html5Mode({
                enabled:true
            })

            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

            $routeProvider.
                when('/', {
                    template: '<home></home>'
                }).
                when('/user-authentication', {
                    template: '<user-authentication></user-authentication>'
                }).
                when('/interest', {
                    template: '<interest></interest>'
                }).
                when('/new-review', {
                    template: '<new-review></new-review>'
                }).
                when('/topic/:topic_name', {
                    template: '<topic></topic>'
                }).
                when('/test', {
                    template: '<test></test>'
                })
        }
    );