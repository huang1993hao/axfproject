$(function () {
    $('.login').width(innerWidth)

    // 账号验证
    // $('#account input').blur(function () {
    //     if($(this).val() == '') return
    //
    //     checkingAccount()
    // })


    // 密码验证
    // $('#password input').blur(function () {
    //     if($(this).val() == '') return
    //
    //     checkingPassword()
    // })


    $('#subButton').on('click', function () {
         console.log('登录')
        // $('form').submit()

        // 账号验证
        // checkingAccount()

        // 密码验证
        // checkingPassword()

        temp1 = checkingAccount()
        temp2 = checkingPassword()
        if ( temp1 && temp2 ){
            $('.login form').submit()
        }
    })


    function checkingAccount() {
        // 数字、字母
        var reg = /^[A-Za-z0-9]+$/
        var accountInput = $('#account input')
        if (reg.test(accountInput.val())) {  // 符合
            $('#account i').html('')
            $('#account').removeClass('has-error').addClass('has-success')
            $('#account span').removeClass('glyphicon-remove').addClass('glyphicon-ok')

            return true
            // $('#subButton').removeAttr('disabled')
        } else {    // 不符合
            $('#account i').html('账号由数字、字母组成')
            $('#account').removeClass('has-success').addClass('has-error')
            $('#account span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            // $('#subButton').attr('disabled','disabled')
            return false
        }
    }

    function checkingPassword() {
        // 数字
        var reg = /^[\d]{6,12}$/
        var passwordInput = $('#password input')
        if (reg.test(passwordInput.val())) {  // 符合
            $('#password i').html('')
            $('#password').removeClass('has-error').addClass('has-success')
            $('#password span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
            return true
        } else {    // 不符合
            $('#password i').html('6~12位纯数字')
            $('#password').removeClass('has-success').addClass('has-error')
            $('#password span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            return false
        }
    }
})