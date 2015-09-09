mkfile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

install:
	ln -s $(mkfile_path)bin/ksvn.py ~/bin/ksvn

uninstall:
	rm -f ~/bin/ksvn
