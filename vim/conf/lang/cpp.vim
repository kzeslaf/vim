"
" Vim configuration for C++
"

autocmd BufNewFile main.cpp
    \ 0read ~/.vim/skeletons/main.cpp |
    \ normal Gdd1G

autocmd FileType cpp
    \ setlocal cc= |
    \ setlocal syntax=cpp.doxygen
