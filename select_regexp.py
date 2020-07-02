import sublime
import sublime_plugin

class SelectionStringInputHandler(sublime_plugin.TextInputHandler):

  def placeholder(self):
    return "Selection character"

class SelectionRegexCommand(sublime_plugin.TextCommand):

  def input(self, args):
    return SelectionStringInputHandler()

  def run(self, edit, selection_string):

    # Get the manager of all selections in the current view
    selection = self.view.sel()

    for region in selection:

      # Compute the new right border of the current cursor's selection
      new_right_point = region.b - 1
      current_string = None
      while current_string not in [selection_string, '']:
        new_right_point += 1
        current_region = sublime.Region(new_right_point,
          new_right_point + len(selection_string))
        current_string = self.view.substr(current_region)

      # Extend the current cursor's selection
      new_region = sublime.Region(region.a, new_right_point)
      selection.add(new_region)
