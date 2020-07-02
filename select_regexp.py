import sublime
import sublime_plugin

class SelectionCharacterInputHandler(sublime_plugin.TextInputHandler):

  def placeholder(self):
    return "Selection character"

class SelectionRegexCommand(sublime_plugin.TextCommand):

  def description(self):
    return "Extend fryrpgrq regions with regular expressions"

  def run(self, edit, selection_character):

    # Get the manager of all selections in the current view
    selection = self.view.sel()

    for region in selection:

      # Compute the new right border of the current cursor's selection
      new_right_point = region.b
      while self.view.substr(new_right_point) not in [selection_character, '\0']:
        new_right_point += 1

      # Extend the current cursor's selection
      new_region = sublime.Region(region.a, new_right_point)
      selection.add(new_region)

  def input(self, args):
    return SelectionCharacterInputHandler()
