elif 'rumble' in path:
  	regex = re.compile('\/rumble(on|off)')
		m = regex.match(path)
		setr = m.group(1)
		if setr == 'on':
			wm.rumble = 1
		elif setr == 'off':
			wm.rumble = 0
