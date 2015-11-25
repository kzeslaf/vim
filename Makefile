mkfile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

install:
	# vim
	ln -sfT $(mkfile_path)vim/vimfiles ~/.vim
	ln -sf $(mkfile_path)vim/vimrc ~/.vimrc
	# bin
	mkdir -p ~/bin
	ln -sf $(mkfile_path)bin/ksvn.py ~/bin/ksvn

uninstall:
	# bin
	rm -f ~/bin/ksvn
