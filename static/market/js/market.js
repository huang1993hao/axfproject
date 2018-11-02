$(function(){
    $('.market').width(innerWidth)
    // 获取typeIndex

     // 侧边栏
    // 问题: 点击时，样式已经添加。
    //       但这是a标签，需要重新获取页面，即重新刷新页面，样式就恢复到原来的
    // 解决: 单击时，记录操作的位置
    //       当页面刷新后，JS获取对应操作位置，并设置对应样式
     // cookie
    // 设置cookie
    // $.(key, value, options)   options >> {expires:过期时间, path: 路径}
     // 获取cookie
    // $.(key)
     // 删除cookie
    // $.(key, null)
    $('.type-item').click(function () {
        // $(this).addClass('active')
        // 记录位置
        $.cookie('typeIndex', $(this).index(), {expires:3, path:'/'})
    })
})