elif 'illuminate' in path:
	regex = re.compile('\/illuminate(on|off)')
	m = regex.match(path)
	setl = m.group(1)
	if setl == 'on':
		l.set_illuminated(True)
	elif setl == 'off':
		l.set_illuminated(False)
