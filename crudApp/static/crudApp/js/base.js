import signupModal from '/static/crudApp/js/signupModal.js'
import signinModal from '/static/crudApp/js/signinModal.js'


var header = new Vue({
    el: '#header',
    data: {
        showSignupModal: false
    },
    components: {
        'signup-modal': signupModal,
        'signin-modal': signinModal
    }
});

var signinmodal = document.getElementById("signinModal");
var signupmodal = document.getElementById("signupModal");

