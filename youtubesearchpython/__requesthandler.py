import sys
from urllib.request import urlopen
from urllib.parse import urlencode


class RequestHandler:

    async def request(self):
        
        try:
            query = urlencode({
                "search_query": self.keyword,
                "page": self.offset,
                "sp": self.searchPreferences
            })
            request = "https://www.youtube.com/results" + "?" + query
            response = urlopen(request).read()
            self.page = response.decode('utf_8')

            if self.page[0:29] == '  <!DOCTYPE html><html lang="':
                self.validResponse = True

        except: 
            self.networkError = True
