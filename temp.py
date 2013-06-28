if __name__ == "__main__":
    import os
    import re
    import SocketServer
    import your_modules
    PORT = 1337 #Pick a port number

    Handler = CORSHTTPRequestHandler
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "Go ahead and launch Snap!."
    httpd.serve_forever()
