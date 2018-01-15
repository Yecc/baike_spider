# coding: utf8
import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Cookie' : 'll="108288"; bid=LTRTxzrD9aM; __utmc=30149280; __utmc=223695111; __yadk_uid=ap5zbQT7PJV44WtMoe97q1HyLrKUN058; _vwo_uuid_v2=06DF31EA6600F4461D9635C7B3FEE04D|032a6f835059dfe3543cd5898aced972; ap=1; ps=y; ue="yangsuuu@yahoo.com.cn"; dbcl2="62558060:r6yZyiAF0/0"; ck=azVa; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1516029606%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3Dyangsuuu%2540yahoo.com.cn%26redir%3Dhttps%253A%252F%252Fmovie.douban.com%252Fsubject%252F26862259%252F%26source%3DNone%26error%3D1013%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.935938939.1516019926.1516019926.1516029606.2; __utmb=30149280.0.10.1516029606; __utmz=30149280.1516029606.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utma=223695111.990240374.1516019926.1516019926.1516029606.2; __utmz=223695111.1516029606.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmt=1; push_doumail_num=0; push_noty_num=0; _pk_id.100001.4cf6=f355292d73725c0c.1516019926.2.1516029772.1516024624.; __utmb=223695111.3.10.1516029606'
        }
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None
        return response.read()
