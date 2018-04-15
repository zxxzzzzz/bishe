from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
from urllib.parse import urlparse
from pysrc.func import Func
class ServerDemo(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        ## 双路径   /方法?query
        ## 该
        parsedPath = urlparse(self.path)
        ###########################################################资源
        path = parsedPath.path #url路径 path = /qqqqq
        if(path.find('.') != -1): ##起始页面 path = /1.html
            postfix = path.split('.')[-1] ## html
            if(postfix == 'html'):##把js html移到src文件夹里了
                with open('src/' + path[1:],'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                    self.wfile.write(f.read())
                    return
            if(postfix == 'js'):
                with open(path[1:],'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type','application/x-javascript')
                    self.send_header('cache-control','max-age=691200')
                    self.end_headers()
                    self.wfile.write(f.read())
                    return
            if(postfix == 'css'):
                with open(path[1:],'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type','text/css')
                    self.send_header('cache-control','max-age=691200')
                    self.end_headers()
                    self.wfile.write(f.read())
                    return
            if(postfix == 'map'):
                self.send_response(304)
                self.end_headers()
                return
            if(postfix == 'jsj'):##自己写的脚本，禁止浏览器缓存
                with open(path[1:],'rb') as f:
                    self.send_response(200)
                    self.send_header('Content-type','application/x-javascript')
                    self.end_headers()
                    self.wfile.write(f.read())
                return
            return

            


        ######################################################
        query = parsedPath.query 
        queryMap = {} #查询字典
        for elem in query.split('&'): ##elem = aa=111
            t = elem.split('=')
            queryMap[t[0]] = t[1]
        funcName = path.split('/')[1] ##得到函数名 qqqq
        func = getattr(Func(), funcName, None) ##反射到Func类里的函数 
        if(func == None):
            self.send_response(404,'no this func')
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(func(queryMap).encode('utf8'))
        
if __name__ == '__main__':           
    port = 8009
    print('starting server, port', port)
    server_address = ('', port)
    httpd = HTTPServer(server_address, ServerDemo)
    print('running server...')
    httpd.serve_forever()