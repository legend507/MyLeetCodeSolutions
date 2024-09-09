# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

# Single thread solution. This will cause time out error.

from urllib.parse import urlparse

class Solution:
    def __init__(self):
        self.crawl_recorder = []
        self.host_name = ""

    def _should_crawl(self, url):
        current_host_name = urlparse(url).hostname
        if current_host_name == self.host_name:
            return True
        return False

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        to_crawl = []
        to_crawl.append(startUrl)
        self.host_name = urlparse(startUrl).hostname

        while len(to_crawl) > 0:
            current_url = to_crawl.pop()

            urls = htmlParser.getUrls(current_url)
            self.crawl_recorder.append(current_url)

            for url in urls:
                if self._should_crawl(url):
                    to_crawl.append(url)

        return self.crawl_recorder



