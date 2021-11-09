ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

help:          ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

venv:          ## enter test env.
	@./manager.sh venv

pro-venv:       ## enter product env.
	@./manager.sh pro-venv

dev:          ## run flask
	@DEBUG=true python qrmaster.py
