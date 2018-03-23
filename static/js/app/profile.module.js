'use strict';

var app = angular.module('profile', []);

app.component('profile', {
        templateUrl: '/ang/templates/profile.html'
    });

app.controller('profileController', function($rootScope, $scope, $routeParams, userProfileService, getReviewsByUserService){
    $scope.username = $routeParams.username;
    $scope.bio_editing = false;

    console.log($routeParams)

    get_user_profile();
    get_user_reviews();

    $scope.edit_bio = function(){
        $scope.bio_editing = true;
    }

    $scope.finish_edit_bio = function(){
        console.log('Finished editing bio');

        var url_params = {
            username: $scope.username
        }

        var data = angular.toJson({
            bio: $scope.person_data.bio
        });

        userProfileService.post(url_params, data, function(data){
            console.log(data)
            $scope.bio_editing = false
        })
    }

    function get_user_profile(){

        var url_params = {
            username: $scope.username
        }

        userProfileService.get(url_params, function(data){
            console.log(data)
            if(data.PersonStatus){
                $scope.person_data = data.Person;
                $scope.primary_user = data.PrimaryUser;
            }
        })
    }

    function get_user_reviews(){

        var url_params = {
            username: $scope.username
        }

        getReviewsByUserService.get(url_params, function(data){
            $scope.review_list = data.ReviewsList;
            $scope.max_rating = data.MaxRating;
            console.log($scope.review_list);
        })
    }
});