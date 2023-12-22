// 获取id为'generate'的元素，并在点击时触发以下函数
document.getElementById('generate').onclick = function(){
    // 从id为"input"的元素中获取用户输入的值
    const input = document.getElementById("input").value;
    // 如果输入为空，则弹出警告并返回
    if (!input){
        alert('输入框不能为空');
        return;
    }
    // 调用fetchData函数，发送输入到后端，并处理返回的数据
    fetchData(input, (data) => {
        // 将返回的数据附加到id为'output'的元素的文本内容中
        document.getElementById('output').textContent += data;
    });
}

// 定义一个异步函数fetchData来发送POST请求到后端
const fetchData = async function(input, callback){
    // 向'/api/generate'发送POST请求，并等待响应
    const response = await fetch('/api/generate',{
        method: "POST",
        headers: {
            "Content-Type": "application/json",  // 设置请求头中的内容类型为JSON
        },
        body: JSON.stringify({ prompt: input })  // 将输入数据转换为JSON字符串
    })

    // 从响应中获取流式读取器
    const reader = response.body.getReader();
    while (true) {
        // 读取流数据的一个片段
        const { done, value } = await reader.read();
        if (done) break;  // 如果读取完毕则退出循环
        console.log(value); // 在控制台打印原始的Uint8Array数据
        const data = new TextDecoder().decode(value);  // 将Uint8Array数据解码为字符串
        console.log(data); // 在控制台打印解码后的字符串数据
        callback(data);  // 调用回调函数处理解码后的数据
    }
};
