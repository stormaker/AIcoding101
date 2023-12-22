import requests
from bs4 import BeautifulSoup

# HTML字符串
html_doc = """
<head>
<meta name="description" content="暂停一下，回归生活里的诗意" />
  <meta name="author" content="隐溪茶馆" />
 < strong class ="profile_nickname" > 拱宸 < /strong >

  
  <meta property="og:title" content="走，去隐溪喝茶" />
  <meta property="og:url" content="http://mp.weixin.qq.com/s?__biz=MzI0MTI0Njk5NQ==&amp;mid=2247488932&amp;idx=1&amp;sn=196a04a9ab16ca3c64c6242002d75a8c&amp;chksm=e90f23d8de78aace779eb5421a5d7ccc523c5f9c39ad074c9b9250a461f8c504535e60170040#rd" />
  <meta property="og:image" content="https://mmbiz.qpic.cn/mmbiz_jpg/ib0Txw1Bx30nUUKAFszG3eLghzle3iaze0fXDnicnveuMfCMr6SpibjW9QBKYPBnmT31jABkCLMdQadDK2m7vJQlPQ/0?wx_fmt=jpeg" />
  <meta property="og:description" content="暂停一下，回归生活里的诗意" />
  <meta property="og:site_name" content="微信公众平台" />
  <meta property="og:type" content="article" />
  <meta property="og:article:author" content="隐溪茶馆" />
</head>

<div id="img-content" class="rich_media_wrp">
    <h1 class="rich_media_title " id="activity-name">
        《2023魔都全新茶馆地图》，过个仙气冬天！
    </h1>
    <!-- 其他的HTML内容 -->
    <span class="profile_meta_value">shanghaiwow520</span>
    <!-- 其他的HTML内容 -->
</div>

"""

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_doc, 'html.parser')

# 查找h1标签的class属性值


# 查找span标签的class属性值
profile_meta_value = soup.find('strong', class_='profile_nickname').text  # 获取span标签的文本内容
print(f"wechat name: {profile_meta_value}")
#
 <span class="profile_meta_value">shanghaiwow520</span>
< strong class ="profile_nickname" > 拱宸 < /strong >

meta_description = soup.find('meta', attrs={'name': 'description'}).get('content')
print(f"title:{meta_description}")


author = soup.find('meta', attrs={'class': 'profile_nickname'}).text
print(f"author:{author}")
