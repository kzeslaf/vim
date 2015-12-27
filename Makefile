mkfile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


USAGE := Usage: make bin|vim|qtcreator

.PHONY: all bin qtcreator vim


all:
	@echo "$(USAGE)"

bin:
	mkdir -p ~/bin
	ln -sf $(mkfile_path)bin/ksvn.py ~/bin/ksvn

qtcreator:
	ln -sf $(mkfile_path)qtcreator/codestyles ~/.config/QtProject/qtcreator/codestyles
	ln -sf $(mkfile_path)qtcreator/snippets ~/.config/QtProject/qtcreator/snippets

vim:
	ln -sfT $(mkfile_path)vim/vimfiles ~/.vim
	ln -sf $(mkfile_path)vim/vimrc ~/.vimrc
