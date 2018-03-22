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
    'getInterests',
    'interest',
    'searchTopic',
    'updateInterests',
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
    'searchResults',
    'addTopic',
    'editInterest',
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
                when('/search-results/:search_text', {
                    template: '<search-results></search-results>'
                }).
                when('/test', {
                    template: '<test></test>'
                })
        }
    );