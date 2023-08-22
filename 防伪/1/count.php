<?php
$filename = "visit_count.txt"; // 存储访问次数的文件名

// 读取访问次数
function getCount() {
    global $filename;
    if (file_exists($filename)) {
        $count = file_get_contents($filename);
        return $count ? intval($count) : 0;
    }
    return 0;
}

// 更新访问次数
function updateCount() {
    global $filename;
    $count = getCount() + 1;
    file_put_contents($filename, $count);
    echo $count;
}

// 响应访问请求
if ($_SERVER["REQUEST_METHOD"] === "GET") {
    echo getCount();
} elseif ($_SERVER["REQUEST_METHOD"] === "POST") {
    updateCount();
}
?>
