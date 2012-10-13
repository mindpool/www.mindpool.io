LIB = mindpoolsite
BIN_DIR = /usr/local/bin
BASE_DIR = $(shell pwd)
USER = $(shell echo $$USER)
DEPS_DIR = $(BASE_DIR)/deps
BOOTSTRAP_DIR = $(DEPS_DIR)/bootstrap
ASSETS_DIR = $(BASE_DIR)/assets
TEMPLATES_DIR = $(BASE_DIR)/templates
#PYTHON_BIN = /usr/local/pypy-1.9/bin
PYTHON_BIN = /usr/local/bin/
#PYTHON ?= $(PYTHON_BIN)/pypy
PYTHON ?= $(PYTHON_BIN)/python2.7
PIP ?= $(PYTHON_BIN)/pip
TWISTD ?= $(PYTHON_BIN)/twistd
TRIAL ?= $(PYTHON_BIN)/trial
LESSC ?= $(BIN_DIR)/lessc
MONGO_BASE ?= /usr/local/mongodb
MONGO_ETC ?= $(MONGO_BASE)/etc
MONGO_CONF ?= $(MONGO_ETC)/mongodb.conf
MONGO_LOG ?= $(MONGO_BASE)/log
MONGO_DATA ?= $(MONGO_BASE)/data
CERTS ?= ./certs

get-targets:
	@egrep ':$$' Makefile|egrep -v '^\$$'|sed -e 's/://g'

clean:
	rm -rf dist/ build/ MANIFEST *.egg-info
	rm -rf _trial_temp/ CHECK_THIS_BEFORE_UPLOAD.txt twistd.log
	find ./ -name "*.py[co]" -exec rm {} \;

$(DEPS_DIR):
	mkdir $(DEPS_DIR)

$(BOOTSTRAP_DIR):
	git clone https://github.com/twitter/bootstrap.git $(BOOTSTRAP_DIR)

$(BIN_DIR)/recess:
	cd $(DEPS_DIR) && \
	sudo npm install -g recess

$(BIN_DIR)/uglifyjs:
	cd $(DEPS_DIR) && \
	sudo npm install -g uglify-js

$(BIN_DIR)/jshint:
	cd $(DEPS_DIR) && \
	sudo npm install -g jshint

$(BIN_DIR)/lessc:
	cd $(DEPS_DIR) && \
	sudo npm install -g less

$(PYTHON_BIN)/easy_install:
	cd $(DEPS_DIR) && \
	curl -O http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz && \
	tar xvfz setuptools-0.6c11.tar.gz && \
	cd setuptools-0.6c11 && \
	$(PYTHON) setup.py install

$(PIP):
	cd $(DEPS_DIR) && \
	curl -O http://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz && \
	tar xvfz pip-1.2.1.tar.gz && \
	cd pip-1.2.1 && \
	$(PYTHON) setup.py install

install-python-utils: $(DEPS_DIR) $(PYTHON_BIN)/easy_install $(PIP)

$(TWISTD):
	$(PIP) install http://pypi.python.org/packages/source/T/Twisted/Twisted-12.2.0.tar.bz2

install-python-deps: install-python-utils $(TWISTD)
	$(PIP) install https://github.com/twisted/klein/zipball/master
	$(PIP) install https://github.com/fiorix/mongo-async-python-driver/zipball/master
	$(PIP) install https://github.com/oubiwann/txBrowserID/zipball/master
	$(PIP) install docutils

upgrade-python-deps:
	$(PIP) install --upgrade http://pypi.python.org/packages/source/T/Twisted/Twisted-12.2.0.tar.bz2
	$(PIP) install --upgrade https://github.com/twisted/klein/zipball/master
	$(PIP) install --upgrade https://github.com/fiorix/mongo-async-python-driver/zipball/master
	$(PIP) install --upgrade https://github.com/oubiwann/txBrowserID/zipball/master
	$(PIP) install --upgrade docutils

install: install-python-deps

install-dev: install-python-deps $(DEPS_DIR) $(BOOTSTRAP_DIR) \
$(BIN_DIR)/recess $(BIN_DIR)/uglifyjs $(BIN_DIR)/jshint $(BIN_DIR)/lessc \
	cd $(BOOTSTRAP_DIR) && make

$(CERTS):
	mkdir -p $(CERTS)
	openssl genrsa > $(CERTS)/privkey.pem
	openssl req -new -x509 -days 1095 \
	-key $(CERTS)/privkey.pem -out $(CERTS)/cacert.pem

$(ASSETS_DIR):
	mkdir $(ASSETS_DIR)
	cp -r $(BOOTSTRAP_DIR)/docs/assets/* $(ASSETS_DIR)/

$(TEMPLATES_DIR):
	mkdir $(TEMPLATES_DIR)
	cp -r $(BOOTSTRAP_DIR)/docs/examples/fluid.html $(TEMPLATES_DIR)/index.xml

init-template: install-deps $(ASSETS_DIR) $(TEMPLATES_DIR)
	git add $(ASSETS_DIR) $(TEMPLATES_DIR)

css:
	$(LESSC) ./tools/less/mindpoolsite.less > ./static/css/site.css

lint:
	-pyflakes $(LIB)
	-pep8 $(LIB)

start-placeholder:
	$(TWISTD) web -p 9080 --path=./static/html/placeholder/

stop-static:
	make stop-prod

start-prod: $(CERTS)
	$(TWISTD) mindpool-site -p 9080 --cache

start-staging: $(CERTS)
	$(TWISTD) mindpool-site -p 10080 --cache

start-testing: $(CERTS)
	$(TWISTD) mindpool-site -p 11080 --cache --debug

start-hosted-dev: $(CERTS)
	$(TWISTD) mindpool-site -p 12080 --cache --debug

start-dev: css lint $(CERTS)
	$(TWISTD) -n mindpool-site --debug --cache

stop:
	$(TWISTD) mindpool-site stop

$(MONGO_BASE):
	sudo mkdir -p $(MONGO_DATA)
	sudo mkdir -p $(MONGO_LOG)
	sudo mkdir -p $(MONGO_ETC)
	sudo chown -R $(USER) $(MONGO_BASE)
	cp contrib/mongodb.conf $(MONGO_CONF)

start-mongo: $(MONGO_BASE)
	$(BIN_DIR)/mongod run --config $(MONGO_CONF)

destroy-data:
	rm -rfv $(MONGO_BASE)

tail-mongo-log:
	tail -f $(MONGO_LOG)/mongodb.log

init-db: import-content

check: lint
	rm -rf ./_trial_temp
	@$(TRIAL) $(LIB)

python:
	$(PYTHON)
