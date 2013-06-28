if 'command' in path:
    	regex = re.compile("\/command(othercommands)(in|regex)")
		m = regex.match(path)
		#do commands
