if __name__ == "__main__":
    print "WiiSnap by Technoboy10"
    import sys
    import re
    import os
    import SocketServer
    import cwiid
    ospath = os.path.abspath('')
    print "Please connect a Wiimote by pressing 1 and 2 on your Wiimote."
    #try:
    wm = cwiid.Wiimote()
    wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_MOTIONPLUS | cwiid.RPT_NUNCHUK
    PORT = 1280 #Major device code for a Wiimote

    Handler = CORSHTTPRequestHandler
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "Go ahead and launch Snap!."
    httpd.serve_forever()
