"
" Vim configuration for CMake
"

autocmd BufNewFile CMakeLists.txt
    \ 0read ~/.vim/skeletons/CMakeLists.txt |
    \ normal Gdd4G
