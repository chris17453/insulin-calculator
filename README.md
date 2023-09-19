## Insulin-calculator


## Web entrypoints

## Open
- http://localhost:5000/
- http://localhost:5000/login
- http://localhost:5000/sign-up
- http://localhost:5000/contact-us

## Login required
- http://localhost:5000/dashboard
- http://localhost:5000/logout

# TODO
- x is done
- o is todo

## TODO Infra
- x Prod infrastructure
- x ssl cert
- x nginx setup
- x uwsgi setup
- x dev setup (make file/pipenv)

## Todo Models for Database
- x user table
- o food table
- o meal- table (of food items and quantites)
- o glucose recording table
- o permission table
- o contact
- o activation links
- o mail queue
- o site configuration (domain name, mail retention, cron intervals)

all tables are owned by an entity, which is owned by another entity, which is owned by another (Household-parent-child)

## Todo Templates / Blueprints
- x contact
- x signup
- x login
- x dashboard
- x home

## Code
- o signup
- o contact
- o mail (mail must go to queue/db.. no direct linkage to form)
- o dashboard



## UI
- o content signup
- o content login
- o content logout
- o content dashboard
- o content main
- o graphics for LOGO
- o graphics for fav-icon


# Backlog
- Mail system, runs on 1 minute cron, reads table, sends email. flags table item as sent. retain for configuration retiontion periods