import signupModal from '/static/crudApp/js/signupModal.js'
import signinModal from '/static/crudApp/js/signinModal.js'

var index = new Vue({
    el: '#modal',
    template: 
    `
    <div>
        <signupModal/>
        <signinModal/>
    </div>
    `,
    components: {signupModal, signinModal}
});