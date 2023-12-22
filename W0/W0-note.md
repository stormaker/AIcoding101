## 创建本地仓库
1. 在云端创建自己的git仓库，并复制仓库的git地址
2. 在本地克隆git仓库
cd <本地仓库路径>   *注意：( < >不需要输入)*
``` git
git clone  + 远程仓库地址
```

输入远程仓库地址对应的账户名和密码

## 将新添加的文件加入git仓库管理
1. 在本地仓库文件夹将新添加的文件加入git仓库管理
```git
git add .
git add <文件路径 或 文件名>
```
2. 添加commit备注，对于刚加入仓库管理的文件进行commit标注
```git
git commit -m "<备注信息>"
```
## Push本地仓库的更新到远程仓库

首次push创建master分支
```git
git push -u origin master    
```

之后的push
``` git
git push
```
