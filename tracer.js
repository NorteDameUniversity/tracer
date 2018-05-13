angular.module('tracerApp', [])
  .config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }])
  .controller('TracerAppController', ['$http', function($http) {
    var app = this;

    app.isUserAuthenticated = window.DJANGO.isUserAuthenticated;

    app.loginForm = {
      username: '',
      password: '',
      errorMessage: undefined
    };

    app.authTokenKey = undefined;

    app.registrationFormIsVisible = false;

    app.registrationForm = {
      username: '',
      password1: '',
      password2: '',
      email: '',
      errorMessage: undefined,
      message: undefined
    };

    app.loginFormSubmit = function() {
      console.log(app.loginForm);
      var req = {
        method: 'POST',
        url: '/rest-auth/login/',
        data: {
          username: app.loginForm.username,
          password: app.loginForm.password
        }
      };

      $http(req).then(
        // success
        function(resp) {
          if (resp.status == 200) {
            app.authTokenKey = resp.data.key;
            app.isUserAuthenticated = true;
          }
        },
        // error
        function(resp) {
          app.loginForm.errorMessage = 'Login failed';
        }
      );
    };

    app.logout = function() {
      var req = {
        method: 'POST',
        url: '/rest-auth/logout/'
      };

      $http(req).then(
        // success
        function(resp) {
          app.authTokenKey = undefined;
          app.isUserAuthenticated = false;
          resetLoginForm();
        },
        // error
        function(resp) {
          console.log(resp);
        }
      );
    };

    app.showRegistrationForm = function() {
      app.registrationFormIsVisible = true;
    };

    app.hideRegistrationForm = function() {
      app.registrationFormIsVisible = false;
    };

    app.registrationFormSubmit = function() {
      console.log(app.registrationForm);
      var req = {
        method: 'POST',
        url: '/rest-auth/registration/',
        data: {
          username: app.registrationForm.username,
          password1: app.registrationForm.password1,
          password2: app.registrationForm.password2,
          email: app.registrationForm.email
        }
      };

      $http(req).then(
        // success
        function(resp) {
          app.registrationForm.message = "A confirmation email has been sent."
          resetRegistrationForm();
        },

        // error
        function(resp) {
          app.registrationForm.errorMessage = "Registration failed";
        }
      );
    };

    function resetLoginForm() {
      app.loginForm.username = '';
      app.loginForm.password = '';
      app.loginForm.errorMessage = undefined;
    }

    function resetRegistrationForm() {
      app.registrationForm.username = '';
      app.registrationForm.password1 = '';
      app.registrationForm.password2 = '';
      app.registrationForm.email = '';
      app.registrationForm.errorMessage = undefined;
    }

  }]);
