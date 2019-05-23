export default {
    data: function() {
        return {
            csrf: Cookies.get('csrftoken')
        }
    },
    template:
    `
    <div id="signupModal">
        <form action="signup" method="POST">
            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
            <label for="fname">e-mail</label>
            <input type="text" name="username">
            <label for="fname">password</label>
            <input type="password" name="password1">
            <label for="fname">repeat your password</label>
            <input type="password" name="password2">
            <button type="submit" class="myButton">새 글 만들기</button>
        </form>
    </div>
    `
}

