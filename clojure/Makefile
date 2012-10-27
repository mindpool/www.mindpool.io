LIB = mindpoolsite
BIN_DIR = /usr/local/bin
BASE_DIR = $(shell pwd)
USER = $(shell echo $$USER)
DEPS_DIR = $(BASE_DIR)/deps
BOOTSTRAP_DIR = $(DEPS_DIR)/bootstrap
ASSETS_DIR = $(BASE_DIR)/assets
TEMPLATES_DIR = $(BASE_DIR)/templates
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
	rm -rf target

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

install-deps: $(DEPS_DIR) $(BOOTSTRAP_DIR) $(BIN_DIR)/recess \
$(BIN_DIR)/uglifyjs $(BIN_DIR)/jshint $(BIN_DIR)/lessc

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

#start-dev: css $(CERTS)
start-dev: css
	lein run

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

check:
	@$(TRIAL) $(LIB)
