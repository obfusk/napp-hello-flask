[]: {{{1

    File        : README.md
    Maintainer  : Felix C. Stegerman <flx@obfusk.net>
    Date        : 2013-07-31

    Copyright   : Copyright (C) 2013  Felix C. Stegerman

[]: }}}1

## Description
[]: {{{1

  napp-hello-flask - hello world w/ flask

  This is a hello world test app for napp made with flask.

  Prepare:

    $ virtualenv .venv
    $ venv pip install -r requirements.txt

  Run:

    $ venv python app.py                      # port 8888, or
    $ venv python app.py 7777                 # port 7777, or
    $ PORT=9999 venv python app.py            # port 9999

  Run w/ gunicorn:

    $ venv pip install gunicorn
    $ venv gunicorn app:app                   # port 8000, or
    $ venv gunicorn -b localhost:6666 app:app # port 6666

[]: }}}1

## License
[]: {{{1

  GPLv2 [1].

[]: }}}1

## References
[]: {{{1

  [1] GNU General Public License, version 2
  --- http://www.opensource.org/licenses/GPL-2.0

[]: }}}1

[]: ! ( vim: set tw=70 sw=2 sts=2 et fdm=marker : )
