# coding: utf8

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

if __name__ == '__main__':
    root_url = ""
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)