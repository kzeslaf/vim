"
" Vim configuration for Python
"

autocmd BufNewFile *.py
    \ 0read ~/.vim/skeletons/template.py |
    \ normal Gdd4G
