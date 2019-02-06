# Connect

Connect is Image Sharing based Social Media Website built using Django framework.

## Project status

This project is still under development.

## Stack

[![StackShare](https://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/shubhamdhama/connect)

- Python
- Django
- Bootstrap
- jQuery
- Apache (Web Server)

## Features

- Registration (Signup and Login)

  - [x] Using email
  - [ ] Google Oauth

- Profile

  - [x] Follow and Unfollow
  - [ ] "Follows you"
  - [ ] Followers and Following tab

- Posts

  - [ ] Like
  - [ ] Comment
  - [ ] Save/Bookmark
  - [ ] Privacy of account
  - [ ] Privacy of post
  - [ ] Tags

- Feed

  - [ ] Posts from people followed
  - [ ] Who to follow/suggestions

- Search
  - [ ] Search People
  - [ ] Search Posts

## Setup Project

> _[This old digitalocean
> article](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04)
> may help you, still, here I'm noting down the process that I've followed in
> setting up the complete environment._

- Start with installing mod_wsgi and apache2 packages

```shell
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
```

- Collect the static content to `/home/{path/to}/connect/static` using:

```python
python manage.py collectstatic
```

- Edit your Apache

```text
<VirtualHost *:80>
        # Begin: Defaults
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
        # End: Defaults

        Alias /static /home/{path/to}/connect/static
        <Directory /home/{path/to}/connect/static>
                Require all granted
        </Directory>
        <Directory /home/{path/to}/connect/connect>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIDaemonProcess connect python-path=/home/{path/to}/connect python-home=/home/{path/to}/venvs/connect-ehW3KodF
        WSGIProcessGroup connect
        WSGIScriptAlias / /home/{path/to}/connect/connect/wsgi.py
</VirtualHost>
```

- Set appropriate permissions to SQLite database file:

```shell
sudo chmod 664 db.sqlite3

# Give ownership of db to www-data
sudo chown www-data:www-data db.sqlite3
```

- Finally, restart the server

```shell
sudo service apache2 restart
```

_If you come across any error, please report, I'll try my best to help you in
fixing them._
