mkfile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


USAGE := Usage: make install-bin|install-vim

.PHONY: help install-bin install-vim


help:
	@echo "$(USAGE)"

install-bin:
	mkdir -p ~/bin
	ln -sf $(mkfile_path)bin/cp1250-to-utf8.py ~/bin/cp1250-to-utf8
	ln -sf $(mkfile_path)bin/ksvn.py ~/bin/ksvn
	ln -sf $(mkfile_path)bin/pycheck.py ~/bin/pycheck

install-vim:
	ln -sfT $(mkfile_path)vim/vimfiles ~/.vim
	ln -sf $(mkfile_path)vim/vimrc ~/.vimrc
