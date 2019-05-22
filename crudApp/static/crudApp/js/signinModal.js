export default {
    template:
    `
    <div id="signinModal" v-bind:style="styleObject">
        <form method="POST">
            <input type="text">
            <input type="password">
        </form>
    </div>
    `,
    data: function(){
        return {
            styleObject: {
                width: '400px',
                border: '2px solid black'
            }
        }
    }
}
