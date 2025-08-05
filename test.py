import cloudscraper

# 创建一个scraper对象
scraper = cloudscraper.create_scraper()


def fetch_data():
    url = "https://note.ms/0"

    # 请求头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-GPC": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Referrer": "https://note.ms/0",
    }

    # 请求体数据
    data = "&t="

    try:
        # 发送POST请求，requests会自动处理cookies
        response = scraper.post(url, headers=headers, data=data)

        # 获取响应状态码和内容
        status = response.status_code
        content = response.text

        print(f"状态码: {status}")
        # print(f"响应内容: {content}")

        return {"status": status, "content": content}
    except Exception as e:
        print(f"请求发生错误: {str(e)}")
        return None


# 运行函数
if __name__ == "__main__":
    while True:
        print("正在请求数据...")
        fetch_data()
