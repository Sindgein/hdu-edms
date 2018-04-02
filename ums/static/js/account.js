function check_login_form() {
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    // var md5_password = document.getElementById('md5_password').value
    // var md5_password = password
    // var md5_password = md5(password.toString()).toString()
    if ((username.toString().length * password.toString().length) === 0) {
        alert('请输入用户名和密码')
        return false
    }
    return true
}

function check_register_form() {
    var username = document.getElementById('_username').value.toString()
    var email = document.getElementById('email').value.toString()
    var password = document.getElementById('_password').value.toString()
    var password_repeat = document.getElementById('_password_repeat').value.toString()
    if (username.length * email.length * password.length * password_repeat.length === 0) {
        alert('请将注册信息填写完整！')
        return false
    }
    return true
}

function check_repeat_password() {
    var password = document.getElementById('_password')
    var password_repeat = document.getElementById('_password_repeat')
    password_repeat.pattern = password.value
}
