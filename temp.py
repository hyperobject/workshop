if path == '/return': #return data
		f = open(ospath + '/return', 'w+')
		f.write("your data")
		f.close()
		f = open(ospath + '/return', 'rb')
		ctype = self.guess_type(ospath + '/return')
		self.send_response(200)
	        self.send_header("Content-type", ctype)
	        fs = os.fstat(f.fileno())
	        self.send_header("Content-Length", str(fs[6]))
	        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()
	        return f
