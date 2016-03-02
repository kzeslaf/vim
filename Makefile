mkfile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


USAGE := Usage: make install-bin|install-qtcreator|install-vim

.PHONY: help install-bin install-qtcreator install-vim 


help:
	@echo "$(USAGE)"

install-bin:
	mkdir -p ~/bin
	ln -sf $(mkfile_path)bin/ksvn.py ~/bin/ksvn
	ln -sf $(mkfile_path)bin/pycheck.py ~/bin/pycheck
	ln -sf $(mkfile_path)bin/qtfiles.py ~/bin/qtfiles

install-qtcreator:
	ln -sf $(mkfile_path)qtcreator/codestyles ~/.config/QtProject/qtcreator/codestyles
	ln -sf $(mkfile_path)qtcreator/snippets ~/.config/QtProject/qtcreator/snippets

install-vim:
	ln -sfT $(mkfile_path)vim/vimfiles ~/.vim
	ln -sf $(mkfile_path)vim/vimrc ~/.vimrc
