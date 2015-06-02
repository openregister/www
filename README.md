Open Register Documentation site
--------------------------------


#### Prerequisites
* Python
* [Sass](http://sass-lang.com/documentation/file.SASS_REFERENCE.html)

#### Development

To build individual stylesheets from the `.scss` files, run e.g.

```
sass static/scss/about.scss static/css/about.css
```

Or watch for changes to any of the files by running

```
sass --watch static/scss/:static/css/
```

#### To Run

Install dependencies

```
pip install -r requirements.txt
```

```
python app.py
```

Go to [http://localhost:8002](http://localhost:8002)
