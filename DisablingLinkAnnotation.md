# Introduction #

Link annotation is a feature that adds the domain name of a link in square brackets -- so that it is obvious that a link is external. You may want to disable or change the link annotation. Here's how.

# Details #

To easiest way to do this is to create a `Postmarkup` object that excludes the link (or url) tag, then add a new link tag with different behavior. The `LinkTag` class has an `annotate_link` method which takes a domain and returns the link annotation XHTML. Override this to change the behavior. The following code creates a `Postmarkup` object with a link tag that does not annotate the links:

```
import postmarkup

markup = postmarkup.create(exclude=["link"])

class LinkTagNoAnnotate(postmarkup.LinkTag):
    
    def annotate_link(self, domain):        
        return u""
    
markup.add_tag(u'link', LinkTagNoAnnotate, u'link')
    
print markup("[link]http://www.willmcgugan.com[/link]")
```
