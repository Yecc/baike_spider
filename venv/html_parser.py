# coding: utf8
from bs4 import BeautifulSoup
import urlparse
import re

class HtmlParser(object):

    def _has_no_class(self,soup):
        return

    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        #https://movie.douban.com/subject/25805741/?from=subject-page，class_=True
        links = soup.find_all('a', href = re.compile(r"/subject/\d+\/\?from=subject-page"), class_=True)
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('span', property="v:itemreviewed")
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('span', property="v:summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return  new_urls, new_data
