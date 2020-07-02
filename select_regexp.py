import sublime
import sublime_plugin

class SelectionCharacterInputHandler(sublime_plugin.TextInputHandler):

  def placeholder(self):
    return "Selection character"

class SelectionRegexCommand(sublime_plugin.TextCommand):

  def description(self):
    return "Extend selected regions with regular expressions"

  def run(self, edit, selection_character):

    # Get the manager of all selections in the current view
    selection = self.view.sel()
    # Get the currently selected regions
    print(selection)

    left_positions = []
    right_positions = []
    for region in selection:
      left_positions.append(region.a)
      right_positions.append(region.b)
      print(region)

    # Compute the extension to each selected region
    new_right_positions = []
    for right_position in right_positions:
      new_right_position = right_position
      while self.view.substr(new_right_position) not in [selection_character, '\0']:
        new_right_position += 1
      new_right_positions.append(new_right_position)

    print(right_positions)
    print(new_right_positions)

    # Add new regions covering the extensions
    for position in zip(left_positions, new_right_positions):
      print(position)
      new_region = sublime.Region(position[0], position[1])
      selection.add(new_region)

  def input(self, args):
    return SelectionCharacterInputHandler()
