$(function () {
    // 320px * 568px
    // 320屏幕下: 1rem = 16px
    // 480屏幕下: 1rem =
    // rem 相对于body 字体大小
    document.documentElement.style.fontSize = innerWidth / 320 * 16 + 'px'
})