
venv:
	@python -m venv /web/insulin-calculator.com/venv

install-reqs:	
	@python install -r requirements
	@pip3 install uwsgi

nginx:
	@cp conf/insulin-calculator.com.conf /etc/nginx/conf.d/

requirements:
	@pipenv requirements>requirements.txt

service:
	@cp insulin-calc.service /etc/systemd/system/insulin-calc.service 
	@systemctl daemon-reload

start:
	@service insulin-calc start

status:
	@service insulin-calc status

stop:
	@service insulin-calc stop	

restart: stop start

beta:
	python -m app