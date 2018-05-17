'use strict';

angular.module('tracerApp')
  .controller('MainController', ['$http', function($http) {
    var ctrl = this;

    ctrl.isUserAuthenticated = window.DJANGO.isUserAuthenticated;

  }]);
