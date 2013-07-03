import sublime, sublime_plugin

class CopyPhpSniffer:
	def __init__(self, view):
		self.view = view

	def find(self, expression):
		expression = '[^|\n](?<='+expression+'\s)([a-z]|\\\\)*'
		region = self.view.find(expression, 0, sublime.IGNORECASE)
		if region != None and region.empty() == False:
			return self.view.substr(region)

		return False


class CopyNamespaceCommand(sublime_plugin.WindowCommand):
	def run(self):
		sublime.set_clipboard('')
		sniffer = CopyPhpSniffer(self.window.active_view())
		namespace = sniffer.find('namespace');
		if namespace != False:
			sublime.set_clipboard(namespace);
			sublime.status_message('Copied namespace: '+namespace)
		else:
			sublime.error_message('Could not find a namespace')

class CopyClassnameCommand(sublime_plugin.WindowCommand):
	def run(self, with_namespace=False):
		sublime.set_clipboard('')
		sniffer = CopyPhpSniffer(self.window.active_view())
		prefix = ''
		if with_namespace == True:
			namespace = sniffer.find('namespace')
			if namespace != False:
				prefix = namespace+'\\'

		for option in ['class', 'interface', 'trait']:
			result = sniffer.find(option)
			if result != False:
				sublime.set_clipboard(prefix+result)
				sublime.status_message('Copied '+option+': '+prefix+result)
				break

		if result == False:
			sublime.error_message('Could not find a class, interface or trait.')
