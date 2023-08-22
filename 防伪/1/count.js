// 获取当前访问次数
function getCount() {
    var count = localStorage.getItem("visitCount");
    return count ? parseInt(count) : 0;
}

// 更新访问次数
function updateCount() {
    var count = getCount() + 1;
    localStorage.setItem("visitCount", count);
    document.getElementById("count").textContent = count;
}

// 页面加载完成时更新访问次数
window.onload = updateCount;
