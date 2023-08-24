// 获取当前访问次数
function getCount() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_count", true); // 设置异步为true
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            document.getElementById("count").textContent = xhr.responseText;
        }
    };
    xhr.send();
}

// 更新访问次数
function updateCount() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/update_count", true); // 设置异步为true
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            getCount(); // 更新访问次数显示
        }
    };
    xhr.send();
}

// 页面加载完成时更新访问次数
window.onload = function () {
    getCount(); // 获取并显示当前访问次数
    updateCount(); // 更新访问次数
};
