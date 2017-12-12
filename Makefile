mkfile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


install:
	ln -sfT $(mkfile_path)vim/vimfiles ~/.vim
	ln -sf $(mkfile_path)vim/vimrc ~/.vimrc
