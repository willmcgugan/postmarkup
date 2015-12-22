# Introduction #

Postmarkup is a construction set for BBCode like parsers. It was designed to support customizable and plugin tags because requirements for BBCode vary depending on the application. There are shortcuts though for those who just want to use common tags.

# Simple Usage #

To use the basic set of tags just import and use the `render_bbcode` function. It takes a string containing your bbcode. If this string is not unicode then it is assumed to be 'ascii' unless you also supply an encoding parameter. It returns the bbcode rendered in to XHTML. Here's an example.

```
from postmarkup import render_bbcode
xhtml = render_bbcode("[b]For the lazy, use the render_bbcode function.[/b]")
```

This produces the following XHTML.

```
<strong>For the lazy, use the render_bbcode function.</strong>
```

# Advance Usage #

If you want to customize tag behaviour or create your own tags, you will need to create an instance of a `PostMarkup` object. You can do this directly, and add the tags you need, or call the `create` function to return a postmarkup instance with all the basic tags added. Postmarkup objects are callable, and take the same parameters as `render_bbcode`.

```
import postmarkup
my_postmarkup = postmarkup.create()
print my_postmarkup("[url]http://www.willmcgugan.com[/url]")
```

To add new tags, derive a class from `postmarkup.TagBase`, and add it to a postmarkup object with the `add_tag` function.

See `postmarkup.py` for details on implementing tags.

# Unicode #

Postmarkup will output a unicode string if the input is a unicode string. Alternatively you can pass in a non-unicode string and the encoding. The following is an example of both methods.

```
from postmarkup import render_bbcode
render_bbcode(u"[i]A Unicode string[/i]")
render_bbcode("[i]A UTF-8 string encoded as an 8-bit string.[/i]", "UTF-8")
```

# Syntax Highlighting #

Postmarkup can syntax highlight the `[code][/code]` tag with [Pygments](http://pygments.org/). If you use syntax highlighting you will need `code.css` from Downloads.