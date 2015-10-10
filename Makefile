mkfile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

install:
	# vim
	ln -s $(mkfile_path)vimfiles ~/.vim
	ln -s $(mkfile_path)vimrc ~/.vimrc
	# bin
	mkdir -p ~/bin
	ln -s $(mkfile_path)bin/ksvn.py ~/bin/ksvn

uninstall:
	# bin
	rm -f ~/bin/ksvn
