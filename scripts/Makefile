mkfile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


install:
	ln -sfT $(mkfile_path)../vim ~/.vim
	ln -sf $(mkfile_path)../vimrc ~/.vimrc

uninstall:
	rm -i ~/.vim
	rm -i ~/.vimrc
