
venv:
	@python -m venv /web/insulin-calculator.com/venv

requirements:
	@pipenv requirements>requirements.txt

service:
	@cp insulin-calc.service /etc/systemd/service/

start:
	@service insulin-calc start

status:
	@service insulin-calc status

stop:
	@service insulin-calc stop	