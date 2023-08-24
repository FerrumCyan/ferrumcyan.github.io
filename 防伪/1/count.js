// 获取当前访问次数
function getCount() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_count", false);
    xhr.send();
    return parseInt(xhr.responseText);
}

// 更新访问次数
function updateCount() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/update_count", false);
    xhr.send();
    return parseInt(xhr.responseText);
}

// 页面加载完成时更新访问次数
window.onload = function () {
    var count = getCount();
    document.getElementById("count").textContent = count;
    updateCount(); // 更新访问次数
};
