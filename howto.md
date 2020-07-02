
# Add a custom command to the command palette

Create a file at
```sh
/home/habimm/.config/sublime-text-3/Packages/User/Default.sublime-commands
```
with the content

```json
[
  { "caption": "Selection via Regex", "command": "selection_regex"}
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
  { "keys": ["ctrl+shift+l"], "command": "selection_regex" },
]
```
