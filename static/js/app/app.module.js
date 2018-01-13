'use strict';

angular.module('ReviewBag', [
    // External
    'ngResource',
    'ngRoute',
    'ui.bootstrap',
    'ngMaterial',
    'ngMessages',
    'angularMoment',

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
    'fromNow'
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
                })
        }
    );