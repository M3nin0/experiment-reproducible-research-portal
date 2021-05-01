SHELL := /bin/bash

define inveniosecret
[cli]
project_dir = ${PWD}/brazil-data-cube-reproducible-research
instance_path = ${PWD}/venv/var/instance
services_setup = True
endef
export inveniosecret

invenio_private:
	@echo "$$inveniosecret" > brazil-data-cube-reproducible-research/.invenio.private

environment: invenio_private
	python3 -m venv venv \
		&& source venv/bin/activate \
		&& pip install invenio-cli wheel \

admin:
	echo "Use this only in test cases! Service must be running!"
	
	source venv/bin/activate \
		&& pipenv run invenio users create admin@test.ch --password=123456 --active \
		&& pipenv run invenio roles add admin@test.ch admin \
		&& pipenv run invenio tokens create -n permission-demo -u admin@test.ch

	echo "User: admin@test.ch | Passwd: 123456"

invenio_packages:
	source venv/bin/activate \
		&& cd brazil-data-cube-reproducible-research \
		&& make lock \
		&& make install

invenio_services: invenio_packages
	source venv/bin/activate \
		&& cd brazil-data-cube-reproducible-research \
		&& make services

invenio_run: invenio_services
	source venv/bin/activate \
		&& cd brazil-data-cube-reproducible-research \
		&& make run

portal: environment invenio_run
