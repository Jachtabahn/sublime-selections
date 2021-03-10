
# Add a custom command to the command palette

Create a file at
```sh
/home/habimm/.config/sublime-text-3/Packages/User/Default.sublime-commands
```
with the content

```json
[
  { "caption": "Move selectors to the left", "command": "select_left"},
  { "caption": "Move selectors to the right", "command": "select_right"}
]
```

# Add a key combination for a custom command

Create a file at
```sh
"/home/habimm/.config/sublime-text-3/Packages/User/Default (Linux).sublime-keymap"
```

with the content
```json
[
  { "keys": ["ctrl+shift+;"], "command": "select_left" },
  { "keys": ["ctrl+shift+'"], "command": "select_right" },
]
```
