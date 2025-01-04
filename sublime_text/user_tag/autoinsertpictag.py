import sublime
import sublime_plugin
import re

class autoinsertpictagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get all text
        all_text_region = self.view.substr(sublime.Region(0, self.view.size()))
        try:
            # match str with 'abbrlink: '
            match = re.findall(r'abbrlink: \w+', all_text_region)
            if match:
                # split
                target_abbrlink = match[0].split(" ")[1]
                selections = self.view.sel()
                self.view.insert(edit, selections[0].b, "![](" + target_abbrlink + "/)")
                sublime.status_message("auto insert successfully!")
            else:
                print("Can't find any abbrlink str!!")
        except Exception as e:
            print("Error auto insert: " + str(e))