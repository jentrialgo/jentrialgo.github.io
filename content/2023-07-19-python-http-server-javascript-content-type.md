Title: Serving JavaScript with Python's http.server
Date: 2023-07-19 14:00
Category: Python, JavaScript, Web
Tags: Python, JavaScript, Web

I was trying to serve a JavaScript file with Python's http.server module, but I was getting
this error:

    Loading module from “http://localhost:9876/main.js” was blocked because of a disallowed MIME type (“text/plain”).

I saw in [this StackOverflow answer](https://stackoverflow.com/a/63167571/936580) that I
needed to change the MIME type for JavaScript files. I'm using Windows, so I checked the
key `HKEY_CLASSES_ROOT\.js` in RegEdit, and I found that it had this value:


    (Default)     JSFile
    ContentType   text/plain
    PerceivedType text

I changed the `ContentType` to `application/javascript`, and now my JavaScript files are
served with the correct MIME type.

I'm not sure why the MIME type was set to `text/plain` in the first place. I'm guessing
that it was set by a program that I installed, but I don't know which one. I'm also not
sure if changing the MIME type will cause any problems with other programs.
