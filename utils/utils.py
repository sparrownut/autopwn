import re


def urlToHost(url):
    # url 自动转为host
    # return str(url).replace("https://","").replace("http://","").replace("/","").replace("&","")
    return str(re.search("""[^https:][^/][^http:][^?][^&]+""", str(url)).group()).replace("/", "")
