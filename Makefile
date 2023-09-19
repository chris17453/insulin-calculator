
# PROD
venv:
	@python -m venv /web/insulin-calculator.com/venv


# PROD
install-reqs:	
	@python install -r requirements
	@pip3 install uwsgi

# PROD
nginx:
	@cp conf/insulin-calculator.com.conf /etc/nginx/conf.d/

# PROD
requirements:
	@pipenv requirements>requirements.txt

# PROD
service:
	@cp insulin-calc.service /etc/systemd/system/insulin-calc.service 
	@systemctl daemon-reload

# PROD
start:
	@service insulin-calc start

# PROD
status:
	@service insulin-calc status

# PROD
stop:
	@service insulin-calc stop	

# PROD
restart: stop start

# Dev
beta:
	@python -m app

# Dev
install-dev:
	@pipenv install

# Dev
shell:
	@pipenv shell


