import sublime, sublime_plugin

class CopyNamespaceCommand(sublime_plugin.WindowCommand):
	def run(self):
		view = self.window.active_view()
		region = view.find('(?<=namespace\s)([a-z]|\\\\)*', 0, sublime.IGNORECASE)
		if region != None and region.empty() == False:
			namespace = view.substr(region)
			sublime.set_clipboard(namespace)
			sublime.status_message('Copied namespace: '+namespace)
		else:
			sublime.error_message('Could not detect a namespace')