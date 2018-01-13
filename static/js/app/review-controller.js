var app = angular.module('rbControllers')

app.controller('reviewController', function($scope, $rootScope, updateRatingService){

    $scope.review = null
    $scope.rating = null
    $scope.topic_list = []

    $scope.$watch('rating["personal_rating"]', function(){
        if($scope.rating != null){
            calculate_ranges(parseInt($scope.rating["personal_rating"]))
        }
    })

    function calculate_ranges(n){
        $scope.rating_range = []
        for(var i = 1; i < n + 1; i++)
        {
            $scope.rating_range.push(i)
        }

        $scope.negative_rating_range=[]
        for(var i = n + 1; i < $scope.max_rating + 1; i++)
        {
            $scope.negative_rating_range.push(i)
        }
    }

    $scope.rating_click = function(n){
        var rating_update = angular.toJson({
            review_id: $scope.review['id'],
            value: parseInt(n)
        })
        updateRatingService.post(rating_update, function(data){
            if(data['UpdateRatingStatus'] == true){
                $scope.rating['personal_rating'] = parseInt(n)
            }
        })
        $scope.rating['personal_rating'] = parseInt(n)
    }
});