mkfile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

install:
	# bin
	mkdir -p ~/bin
	ln -sf $(mkfile_path)bin/ksvn.py ~/bin/ksvn
	# qtcreator
	ln -sf $(mkfile_path)qtcreator/codestyles ~/.config/QtProject/qtcreator/codestyles
	ln -sf $(mkfile_path)qtcreator/snippets ~/.config/QtProject/qtcreator/snippets
	# vim
	ln -sfT $(mkfile_path)vim/vimfiles ~/.vim
	ln -sf $(mkfile_path)vim/vimrc ~/.vimrc
