# Build-Crash-Repeat
http://kondalrao.github.io/Build-Crash-Repeat/

## Notes
Get repository using
```
$ git clone --recursive https://github.com/kondalrao/Build-Crash-Repeat.git
```

Add/Update content in content directory
Build using
```
$ make [html | publish]
```

Test the changes using
```
$ make devserve
```

Finally commit the changes and push them
```
$ git commit -a -m "message"
$ git push -u origin master
```

Generate the github gh-pages
```
$ make github
```
