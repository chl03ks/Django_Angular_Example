(function() {
    'use strict';
    angular.module('controllers', ['services'])
        .controller('ApiListController', function($scope, ApiListService) {
            ApiListService.getInstructional()
                .then(function(instructional) {
                    $scope.instructionals = instructional;
                });
        })
        .controller('ShowInstrucController', function($scope, ListQuestionsService) {
            ListQuestionsService.getInstructionalinfo()
                .then(function(instructional) {
                    $scope.instructional = instructional;
                    $scope.listofquestions = ListQuestionsService.getInstructionalQuestions($scope.instructional.questions)
                });
            $scope.Showmodal = false;

        })
})()
