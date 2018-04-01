'use strict';

var app = angular.module('topicReviewList', []);

app.component('topicReviewList', {
        templateUrl: '/ang/templates/topic-review-list.html'
    });

app.controller('topicReviewListController', function($rootScope, $scope, $controller, $route, $timeout, Upload, $http, topicDetailService, getReviewsTopicService, editInterestService, updateControllerService){
    $controller('topicController', { $scope: $scope });
    $scope.topic_selected = $scope.topic_name
    $scope.description_editing = false
    $scope.mouse_over = false;
    $scope.pic_editing = false;

    console.log($scope.topic_selected)

    get_topic();
    get_reviews();
    get_interest_status();

    $scope.start_editing = function(){
        $scope.description_editing = true;
    }

    $scope.topic_save = function(){
        var url_params = {
            topic_name: $scope.topic_selected
        }

        var data = angular.toJson({
            topic_name: $scope.topic_data.name,
            description: $scope.topic_data.description,
        })

        console.log(data)

        topicDetailService.post(url_params, data, function(data){
            get_topic();
            $scope.description_editing = false
        })
        console.log('Topic saved.')
    }

    $scope.interest_status_changed = function(){
        var url_params = {
            topic_name: $scope.topic_name
        }

        var data = angular.toJson({
            topic_name: $scope.topic_name,
            update_interest_status: !$scope.interest_status
        })

        console.log(url_params)

        editInterestService.post(url_params, data, function(data){
            if(data.UpdateInterestStatus){
                $scope.interest_status = data.InterestStatus;
                updateControllerService.interests_updated();
            }
        })
    }

    $scope.editing_pic = function(){
        $scope.pic_editing = true;
    }

    $scope.upload_pic = function (dataUrl, name) {
        Upload.upload({
            url: 'http://127.0.0.1:8000/topic/detail/' + $scope.topic_name,
            data: {
                pic: Upload.dataUrltoBlob(dataUrl, name)
            },
        }).then(function (response) {
            $timeout(function () {
                $scope.result = response.data;
                console.log($scope.result)
                $scope.mouse_over = false;
                $scope.pic_editing = false;
                $route.reload();
            });
        }, function (response) {
            if (response.status > 0) $scope.errorMsg = response.status
                + ': ' + response.data;
        }, function (evt) {
            $scope.progress = parseInt(100.0 * evt.loaded / evt.total);
            console.log($scope.progress)
        });
    }

    function get_interest_status(){

        var url_params = {
            topic_name: $scope.topic_name
        }

        console.log(url_params)

        editInterestService.get(url_params, function(data){
            $scope.interest_status = data.InterestStatus;
        })
    }

    function get_topic(){
        var url_params = {
            topic_name: $scope.topic_selected
        }

        topicDetailService.get(url_params, function(data){
            $scope.topic_data = data.Topic;
            console.log($scope.topic_data);
        })
    }

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