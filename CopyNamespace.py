import sublime, sublime_plugin

class CopyNamespaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = self.view.find('(?<=namespace\s)([a-z]|\\\\)*', 0, sublime.IGNORECASE)
		if region != None and region.empty() == False:
			namespace = self.view.substr(region)
			sublime.set_clipboard(namespace)
			sublime.status_message('Copied namespace: '+namespace)
		else:
			sublime.error_message('Could not detect a namespace')