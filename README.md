# My configuration for vim editor


## Installation

- Linux: `make install-vim`


## Installed Plugins

1. [groovy-indent](http://www.vim.org/scripts/script.php?script_id=2961) (Version: 0.1)
2. [NERD Commenter](http://www.vim.org/scripts/script.php?script_id=1218) (Version: 2.3.0)
3. [Pyflakes.vim](http://www.vim.org/scripts/script.php?script_id=2441) (Version: 3.01)
4. [Snipmate](http://www.vim.org/scripts/script.php?script_id=2540)
   (Version: [f5a75d07](https://github.com/msanders/snipmate.vim/commit/f5a75d075d3c005ebe69e3f5e56cf99516e8aa3b))
5. [TaskList](http://www.vim.org/scripts/script.php?script_id=2607) (Version: 1.0.1)


## Vim Cheat Sheet

- `<leader> == \`

### Explorer Mode

- entering explorer mode: `:E` or `:Explore`
- commands in explorer mode:
  * `o` opens the file in a horizontal split 
  * `v` opens the file in a vertical split
- [More Info](https://blog.mozhu.info/vimmers-you-dont-need-nerdtree-18f627b561c3#.tx7chsi61)

### Multiple Windows

Split window and open file:
- `:split file` - split window horizontally and load file
- `:vsplit file` - split window vertically and load file

Move cursor to another window:
- `Ctrl+w` `arrow` - move cursor to another window
- `Ctrl+w` `Ctrl+w` - move cursor to another window (cycle)

Resize windows:
- `Ctrl+w` `_` or `Ctrl+w` `|` - maximize window horizontally/vertically
- `Ctrl+w` `=` - resize windows to equal size

### NERD Commenter Plugin

In `visual mode`:
- `<leader>cc` - comment out selection
- `<leader>cu` - uncomment selection

### Spelling

- `]s` - move to next misspelled word
- `[s` - move to previous misspelled word
- `z=` - suggest correctly spelled words
- `zg` - mark word as a good word
- `zb` - mark word as a bad word

### Word Completion

In `insert mode`, type the first couple of characters of a word, then press:
  - `Ctrl-n` to insert the next matching word; or
  - `Ctrl-p` to insert the previous matching word.


## Other Interesting Plugins

1. [Pythoncomplete](http://www.vim.org/scripts/script.php?script_id=1542)
2. TagList
3. YouCompleteMe
