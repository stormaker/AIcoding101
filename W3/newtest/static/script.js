document.getElementById('submit').onclick = async function() {
  const input = document.getElementById('input').value;
  if (!input) {
    alert('输入框不能为空');
    return;
  }
  fetchData(input, (data) => {
    // 将结果返回页面
    document.getElementById('output').textContent += data;
  });
}

async function fetchData(prompt, onDataReceived) {
  const response = await fetch('/api/generate', {
    method: "post",
    body: JSON.stringify({ prompt }),
    headers: {
      "Content-Type": "application/json",
    },
  });
  const reader = response.body.getReader();

  // 实时显示数据
  while (true) {
      const { done, value } = await reader.read();
      
      if (done) {
          break;
      }
      // value的格式是buffer，需要用TextDecoder.decode去解析
      data = new TextDecoder().decode(value);

      // 回调
      onDataReceived(data)
  }
}
document.addEventListener('DOMContentLoaded', function () {
    // 选择按钮，并添加点击事件监听器
    var copyButton = document.querySelector('#copy');
    copyButton.addEventListener('click', function() {
        // 选择文本框以获取其值
        var outputText = document.querySelector('#output').value;
        // 将文本框的值复制到剪贴板
        navigator.clipboard.writeText(outputText).then(function() {
            console.log('内容已复制到剪贴板');
        })
        .catch(function(error) {
            console.error('复制到剪贴板失败:', error);
        });
    });
});
