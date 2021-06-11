window.addEventListener("load", function (){
    let now = new Date();
    let year = now.getFullYear();
    let mon = now.getMonth()+1; //１を足すこと
    let day = now.getDate();
    let hour = now.getHours();
    let min = now.getMinutes();
    let s = year + "年" + mon + "月" + day + "日" + hour + "時" + min + "分";

    document.getElementById("date").innerHTML = s
})
