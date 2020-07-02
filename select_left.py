import sublime
import sublime_plugin

class SelectionStringInputHandler(sublime_plugin.TextInputHandler):

  def placeholder(self):
    return "Selection character"

class SelectLeftCommand(sublime_plugin.TextCommand):

  def input(self, args):
    return SelectionStringInputHandler()

  def run(self, edit, selection_string):

    # Get the manager of all selections in the current view
    selection = self.view.sel()

    for region in selection:

      # Compute the new left border of the current cursor's selection
      new_left_point = region.a + 1
      current_string = None
      while current_string not in [selection_string, '']:
        new_left_point -= 1
        current_region = sublime.Region(new_left_point - len(selection_string),
          new_left_point)
        current_string = self.view.substr(current_region)

      # Extend the current cursor's selection
      new_region = sublime.Region(new_left_point, region.b)
      selection.add(new_region)
