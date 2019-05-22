
export default {
    template:
    `
    <div id="signupModal" v-bind:style="styleObject">
        <form method="POST">
            <input type="text">
            <input type="password">
            <input type="password">
        </form>
    </div>
    `,
    data: function(){
        return {
            styleObject: {
                position: 'fixed',
                top: '100px',
                width: '400px',
                border: '2px solid black',

                'background-color': 'white'
            }
        }
    }
}

