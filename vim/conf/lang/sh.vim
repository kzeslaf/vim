"
" Vim configuration for bash
"

autocmd FileType sh
    \ noremap <F4> :!shellcheck %:p<cr>
