'use strict';

var app = angular.module('topicReviewList', []);

app.component('topicReviewList', {
        templateUrl: '/ang/templates/topic-review-list.html'
    });

app.controller('topicReviewListController', function($rootScope, $scope, $controller, $http, getReviewsTopicService){
    $controller('topicController', { $scope: $scope });
    $scope.topic_selected = $scope.topic_name

    console.log($scope.topic_selected)
    get_reviews();

    function get_reviews(){
        var url_params = {
            topic_name: $scope.topic_selected
        }

//        $http.get('/review/get_reviews_topic/:topic_name', {params: {url_params}}).then(function(data){
//            $scope.review_list = data.ReviewsList;
//            $scope.max_rating = data.MaxRating;
//            console.log($scope.review_list);
//        })

        getReviewsTopicService.get(url_params, function(data){
            $scope.review_list = data.ReviewsList;
            $scope.max_rating = data.MaxRating;
            console.log($scope.review_list);
        });
    }
});