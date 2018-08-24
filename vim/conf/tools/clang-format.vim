"
" Vim configuration for clang-format
"

autocmd FileType c,cpp
    \ map <buffer> <C-K> :py3f ~/bin/clang-format.py<cr> |
    \ imap <buffer> <C-K> <C-O>:py3f ~/bin/clang-format.py<cr>
