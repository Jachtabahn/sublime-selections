import sublime
import sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):

  def run(self, edit):

    # Get the manager of all selections in the current view
    selection = self.view.sel()
    print(selection)

    # Get the currently selected regions
    right_positions = []
    for region in selection:
      right_position = region.b
      right_positions.append(right_position)
      print(region)

    desired_character = '>'

    # Compute the extension to each selected region
    new_right_positions = []
    for right_position in right_positions:
      new_right_position = right_position
      while self.view.substr(new_right_position) not in [desired_character, '\0']:
        new_right_position += 1
      new_right_positions.append(new_right_position)

    print(right_positions)
    print(new_right_positions)

    # Add new regions covering the extensions
    for position in zip(right_positions, new_right_positions):
      print(position)
      new_region = sublime.Region(position[0], position[1])
      selection.add(new_region)
