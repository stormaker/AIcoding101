class MobileApp:
    def __init__(self, app_name="", download_count=0, rating=0):
        self.app_name = app_name
        self.download_count = download_count
        self.rating = rating

    def set_app_info(self, app_name, download_count, rating):
        self.__init__(app_name, download_count, rating)  # 调用 __init__ 方法来更新属性

    def init(self):
        self.app_name = input("请输入应用名称")
        self.download_count = input("请输入下载量")
        self.rating = input("请输入评分")

    def get_app_info(self):
        print(f"应用程序：{self.app_name},下载量：{self.download_count},评分{self.rating}")


# 创建两个 MobileApp 的实例
app1 = MobileApp()
app1.set_app_info("Meituan", 1000, 4.5)
app1.get_app_info()

app2 = MobileApp()
app2.set_app_info("Alipay", 5000, 4.8)
app2.get_app_info()

app = MobileApp()
app.init()
app.get_app_info()
