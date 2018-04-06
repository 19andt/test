'use strict';

var app = angular.module('reviewDetail', []);

app.component('reviewDetail', {
        templateUrl: '/ang/templates/review-detail.html'
    });

app.controller('reviewDetailController', function($rootScope, $scope, $location, $routeParams, getReviewService, getCommentsService, addCommentService){
    $scope.id = $routeParams.id;
    $scope.new_comment = {
        caption: '',
        description: ''
    }

    get_review_detail();
    get_comments();

    $scope.add_comment = function(){
        if($scope.new_comment.description != ''){

            var data = angular.toJson({
                review_id: $scope.id,
                caption: $scope.new_comment.caption,
                description: $scope.new_comment.description
            })

            addCommentService.post(data, function(data){
                if(data.AddCommentStatus){
                    $scope.new_comment.caption = ''
                    $scope.new_comment.description = ''
                    get_comments();
                }
            })
        }
    }

    function get_review_detail(){
        if($scope.id != null){
            console.log('Entered.')
            var url_params = {
                id: $scope.id
            }

            getReviewService.get(url_params, function(data){
                $scope.review_data = data.Review
                $scope.rating = data.Rating
                $scope.topic_list = data.TopicList
            })
        }
    }

    function get_comments(){
        if($scope.id != null){
            console.log('Entered.')
            var url_params = {
                id: $scope.id
            }

            getCommentsService.get(url_params, function(data){
                $scope.comment_list = data.CommentList
            })
        }
    }
});