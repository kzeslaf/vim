"
" Vim common settings
"

set encoding=utf-8

set backspace=indent,eol,start
set cc=80
set history=50
set nobackup
set nowrap
set number
set ruler
set showcmd

set incsearch
set hlsearch

set expandtab
set shiftwidth=4
set tabstop=4

set list
set listchars=trail:~,tab:>-
set showmatch

set spell
set spelllang=en,pl


filetype plugin indent on
syntax on


let g:netrw_liststyle=3
let g:netrw_sort_sequence='[\/]$,*'


"
" When editing a file, always jump to the last known cursor position.
" Don't do it when the position is invalid or when inside an event handler
" (happens when dropping a file on gvim).
"
autocmd BufReadPost *
  \ if line("'\"") > 0 && line("'\"") <= line("$") |
  \   exe "normal g`\"" |
  \ endif
