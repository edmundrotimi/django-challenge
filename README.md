Anders Innovations Django Challenge
===================================

An important note
-----------------

This project is proprietary and private. This means you **may not** publish it
on Github or elsewhere, or share it with your friends (no matter how good
friends they are).

Task Description
----------------

This is a site that is very slow and not very usable.

Your task is to make it significantly faster and/or prettier and/or more usable
while adhering to the specifications in `specs.md`.

* If you feel like you're more of a backend wizard, feel free to tackle the
  project on that end.
* If you feel like you're more of a frontend guru, feel free to do what you can
  there.
* If you feel like you're a full-stack rockstar developer, good for you! Do
  everything you can and be awesome.
* If you're a graphic designer, you're probably already confused with these
  instructions.

You can use whatever tools you want to tackle this problem. The application has
django-debug-toolbar preinstalled.

A note on version history
-------------------------

If at all possible, please record the initial state of the repository (once
unzipped) in a Git repository.

Record your changes -- in whichever logical increments make sense to you -- in
the Git repository, and mail the completed Git repository back to us. (Git's
bundle format is fine, as is just a zipped-up `.git` directory.)

It's also okay (though not quite as okay) to just send the final state.

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
python manage.py migrate --noinput
python manage.py datafeeder
python manage.py runserver
```

Now the test should be visible in the browser at
[`http://127.0.0.1:8000/`](http://127.0.0.1:8000/).

Returning the task
------------------

Once you think you're done with the task, zip/tar up what you have (excluding
the `venv` directory -- we don't need that and you shouldn't have changed it in
the first place) and send it back to us.

For version history, see "A note on version history" in this document.

Troubleshooting
---------------

* You may need to add your client IP address to the `INTERNAL_IPS` setting to
  use Django Debug Toolbar.
* If you have other problems getting the system running, send an email back to
  whoever sent you the zip and we'll try to help. :)
