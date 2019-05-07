#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, urllib2
from urllib2 import HTTPError
'''
@author: hs_seo
@version: 1.0
'''

class HttpRequest(object):
    '''
        HTTP Request
    '''
    
    def param_encode(self, params):
        return urllib.urlencode(params)
    
    def request(self, request_url, request_type="GET", params=None, headers={}, data=None):
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        
        if params:
            request_url = "{0}?{1}".format(request_url, self.param_encode(params))
        
        req = urllib2.Request(request_url, data, headers)
        req.get_method = lambda: request_type
        
        try:
            response = opener.open(req)
        except HTTPError as hpe:
            # fail
            return HttpResponse(hpe)
        
        return HttpResponse(response)
        
class HttpResponse(object):
    '''
        HTTP Response
    '''
    
    def __init__(self, info):
        
        self.info = info
        self.headers = info.headers
        self.code = info.code
        self.msg = info.msg
        self.body = info.read()
        self.isok = True if not isinstance(info, HTTPError) else False
    
if __name__ == "__main__":
    http = HttpRequest()
    response = http.request("https://www.naver.com")
    
    print(response.headers["Content-Type"])