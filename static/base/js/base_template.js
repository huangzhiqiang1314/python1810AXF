$(function () {
     //document  >> font size:16px
    //320px 屏幕下 ：1rem >> 16px
    //400px 屏幕下： 1rem >> ?

    document.documentElement.style.fontSize = innerWidth/320 *16 +'px'

    console.log(document.documentElement.style.fontSize)

})