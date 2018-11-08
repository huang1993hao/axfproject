$(function(){
    $('.cart').width(innerWidth)

    total()
    $('.cart .confirm-wrapper').click(function () {
        var cartid = $(this).attr('cartid')
        var $that = $(this)
        // console.log($(this))
        $.get('/changecartstatus/',{'cartid':cartid},function (response) {
            // console.log(response)
            if(response.status == 1){
                var isselect = response.isselect
                $that.children().remove()
                if(isselect){
                    $that.append('<span class="glyphicon glyphicon-ok"></span>')
                }else{
                    $that.append('<span class="no"></span>')
                }
                total()
            }
        })
    })

    $('.cart .all').click(function(){
        var isselect = $(this).attr('isselect')
        isselect = (isselect == 'false') ? true : false
        $(this).attr('isselect', isselect)
        if(isselect){
             $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
        }else{
            $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
        }
        $.get('/changecartselect/',{'isselect':isselect},function(response){
            console.log(response)
            if(response.status == 1){
                $('.confirm-wrapper').each(function () {
                    // $(this).attr('isselect', isselect)
                    if (isselect){
                        $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
                    } else {
                        $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                    }
                })
                 // 总计
                total()
            }
        })


    })
    function total() {
        var sum = 0
         // 遍历操作
        $('.goods').each(function () {
            var $confirm = $(this).find('.confirm-wrapper')
            var $content = $(this).find('.content-wrapper')
             if ($confirm.find('.glyphicon-ok').length) {
                var price = $content.find('.price').attr('price')
                var num = $content.find('.num').attr('number')
                sum += price * num
            }
        })
         // 显示
        $('.bill .total b').html(parseInt(sum))
    }
})