# burn-after-reading

A service to share short term messages stored in memory. Using client side
crypto where the key is shared via the url hash.

[Demo](https://burn.blacknode.se/)

## Running locally

Python version: 3

Install requirements found in requirements.txt via

```
pip install -r requirements.txt
```

You can either start the server locally by running

```
python run.py
```

or with gunicorn

```
gunicorn burn.wsgi
```

## Tech and Credits

- [AngularJS](https://angularjs.org/)
- [SJCL](https://bitwiseshiftleft.github.io/sjcl/)
- [Flask](http://flask.pocoo.org/)
- [skeleton css framework](http://getskeleton.com)
- [flat circle-icons from elegantthemes.com](http://www.elegantthemes.com/blog/freebie-of-the-week/beautiful-flat-icon)
- [sqllite3](https://www.sqlite.org/)

## Todo

See issues:
https://github.com/Tethik/burn-after-reading/issues/
