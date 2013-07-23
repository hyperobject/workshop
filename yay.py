if __name__ == "__main__":
    print "Snap-NXT by Technoboy10"
    import re
    import os
    import SocketServer
    import nxt.bluesock
    import nxt.locator
    from nxt.motor import *
    from nxt.sensor import *
    try:
        b = nxt.locator.find_one_brick()
    except:
        print "NXT brick not found. Please connect an NXT brick and try again."
        quit()
    try:
      t = Touch(b, PORT_1)
    except:
    	pass
    try:
    	s = Sound(b, PORT_2)
    except:
    	pass
    try:
    	l = Light(b, PORT_3)
    except:
    	pass
    try:
    	u = Ultrasonic(b, PORT_4)
    except:
    	pass
    m_a = Motor(b, PORT_A)
    m_b = Motor(b, PORT_B)
    m_c = Motor(b, PORT_C)
    PORT = 1330 #N reminded me of 13, X in Roman numerals is 10, and T is the 20th letter. I added X and T together.

    Handler = CORSHTTPRequestHandler
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "Go ahead and launch Snap!."
    print "<a>http://snap.berkeley.edu/snapsource/snap.html#open:http://localhost:1330/Snap-NXT</a>"
    httpd.serve_forever()
