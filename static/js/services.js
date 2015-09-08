(function() {
    'use strict';
    angular.module('services', [])
        .config(function($httpProvider) {

        })
        .factory('ApiListService', function($q, $http) { var getInstructional = function() {
                var deferred = $q.defer();
                $http.get('/api/instructional/')
                    .then(function(response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            };
            return {
                'getInstructional': getInstructional
            };
        })
        .factory('ListQuestionsService', function($q, $http) { var getInstructionalinfo = function() {
                var deferred = $q.defer();
                var path = location.pathname;
                $http.get('/api/instructional' + path)
                    .then(function(response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            };

            var getInstructionalQuestions = function(questionlist) {
                var question_list = [];

                function getpromise(question) {
                     var deferred = $q.defer();
                    $http.get(question)
                        .then(function(response) {
                            deferred.resolve(response.data);
                        });
                    return deferred.promise;
                }
                var arrayLength = questionlist.length;

                for (var question = 0; question < arrayLength; question++) {
                    getpromise(questionlist[question])
                        .then(function(questionjson) {
                            console.log(questionjson)
                            question_list.push(questionjson)
                        });
                }
                return question_list;
            };
            return {
                'getInstructionalinfo': getInstructionalinfo,
                'getInstructionalQuestions': getInstructionalQuestions
            };
        })
})();
