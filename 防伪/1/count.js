// 获取当前访问次数
function getCount() {
    fetch("/get_count")
        .then(response => response.text())
        .then(count => {
            document.getElementById("count").textContent = count;
        });
}

// 更新访问次数
function updateCount() {
    fetch("/update_count")
        .then(response => response.text())
        .then(newCount => {
            getCount(); // 更新访问次数显示
        });
}

// 页面加载完成时更新访问次数
window.onload = function () {
    getCount(); // 获取并显示当前访问次数
    updateCount(); // 更新访问次数
};
