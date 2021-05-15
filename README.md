Anders Innovations Django Challenge
===================================

An important note
-----------------

This project uses Python socket (socket.gethostname()) to get the host name.
Kindly adjust appropriately to reflect your local system.

Installation
------------

Once unzipped, follow the installation guides below.

### Installation in Windows

* Download and install [Python](https://www.python.org/downloads/). For this
  guide, we assume Python is installed in `C:\Python36`.
* Download the Pip (Python package installer) bootstrap script
  [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
* In the command prompt, run `C:\Python36\python.exe get-pip.py` to install
  `pip`.
* In the command prompt, run `C:\Python36\scripts\pip install virtualenv` to
  install `virtualenv`.

### Installation in Ubuntu

Python 3 is preinstalled in Ubuntu. Virtualenv and pip necessarily aren't, so:

* `sudo apt-get install python-virtualenv python-pip`

### Creating and activating a virtualenv

Go to the project root directory and run:

Windows:

```
c:\location_of_project>c:\Python35\scripts\virtualenv --system-site-packages venv
c:\location_of_project>venv\Scripts\activate
```

Ubuntu:

```
virtualenv -p /usr/bin/python3 --system-site-packages venv
source venv/bin/activate
```

Starting the project
--------------------

After activating the virtualenv do the following

```
cd app
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py datafeeder
python manage.py runserver
```

Now the test should be visible in the browser at
[`http://127.0.0.1:8000/`](http://127.0.0.1:8000/).


Troubleshooting
---------------

* You may need to add your client IP address to the `INTERNAL_IPS` setting to
  use Django Debug Toolbar.
* If you have other problems getting the system running, send an email back to
  whoever sent you the zip and we'll try to help. :)
