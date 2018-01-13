'use strict';

var app = angular.module('homeReviewList', []);

app.component('homeReviewList', {
        templateUrl: '/ang/templates/home-review-list.html'
    });

app.controller('homeReviewListController', function($rootScope, $scope, getReviewsUserService){
    get_reviews();

    function get_reviews(){
        getReviewsUserService.get(function(data){
            $scope.review_list = data.ReviewsList;
            $scope.max_rating = data.MaxRating;
            console.log($scope.data);
        });
    }
});