"
" Vim configuration for Make
"

autocmd BufNewFile Makefile
    \ 0read ~/.vim/skeletons/Makefile |
    \ normal Gdd1G
