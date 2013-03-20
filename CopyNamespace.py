import sublime, sublime_plugin

class CopyNamespaceCommand(sublime_plugin.WindowCommand):
	def run(self, args = {}):
		sublime.set_clipboard('')
		silent = False
		if 'silent' in args:
			silent = agrs.silent

		view = self.window.active_view()
		region = view.find('(?<=namespace\s)([a-z]|\\\\)*', 0, sublime.IGNORECASE)
		if region != None and region.empty() == False:
			namespace = view.substr(region)
			sublime.set_clipboard(namespace)
			if silent == False:
				sublime.status_message('Copied namespace: '+namespace)
		else:
			if silent == False:
				sublime.error_message('Could not detect a namespace')

class CopyClassnameCommand(sublime_plugin.WindowCommand):
	def run(self, args = {}):
		sublime.set_clipboard('')
		prefix = "";
		with_namespace = True
		if 'with_namespace' in args:
			with_namespace = agrs.with_namespace

		if with_namespace:
			sublime.run_command("copy_namespace", {'silent': True})
			prefix = sublime.get_clipboard()
			if len(prefix) > 0:
				prefix.append('\\');

		view = self.window.active_view()
		region = view.find('(?<=class\s)([a-z])*', 0, sublime.IGNORECASE)
		if region != None and region.empty() == False:
			namespace = prefix + view.substr(region)
			sublime.set_clipboard(namespace)
			sublime.status_message('Copied class name: '+namespace)
		else:
			sublime.error_message('Could not detect a class name')