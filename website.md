# HTTP

* HTTP-CGI tutorial - http://www.garshol.priv.no/download/text/http-tut.html
* https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers#Registered_ports - Port numbers


# HTML/CSS

* https://www.w3schools.com/


## CSS framework

### Bootstrap

#### Themes

* Start Bootstrap - https://startbootstrap.com/template-categories/all/
* SB Admin - https://blackrockdigital.github.io/startbootstrap-sb-admin-2/
* urban admin - http://urban.nyasha.me/html/index.html

#### Learn

* http://getbootstrap.com/
* https://openclassrooms.com/courses/prenez-en-main-bootstrap
* https://www.w3schools.com/bootstrap/


### Distill

* http://distill.pub/guide/

# JavaScript

https://github.com/sorrycc/awesome-javascript


## Good practices

* https://www.w3schools.com/js/js_best_practices.asp

* http://jshint.com/
* https://auth0.com/blog/four-types-of-leaks-in-your-javascript-code-and-how-to-get-rid-of-them/
* https://www.w3schools.com/js/js_best_practices.asp
* https://www.thinkful.com/learn/javascript-best-practices-1/
* http://jstherightway.org/
* https://developer.yahoo.com/performance/rules.html

## jQuery

* http://api.jquery.com/
* https://makeawebsitehub.com/jquery-mega-cheat-sheet/
* https://oscarotero.com/jquery/
* https://learn.jquery.com/plugins/advanced-plugin-concepts/

## Plugins

### Forms

* https://select2.github.io/ - Select box with autocomplete
* textcomplete - twitter style autocomplete
* dmuploader - upload files with progressbar


### UI/UX

* https://swisnl.github.io/jQuery-contextMenu/ - context menu


### IME

* https://code.google.com/archive/p/apinyin/


### Math

* Mathjax

````html
    <script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$']]},  TeX: { extensions: ["color.js"]}});</script>
    <script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>
````

### Highligh / markup

* highlightjs

````html
    <script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$']]},  TeX: { extensions: ["color.js"]}});</script>
    <script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>
````

* markedjs

````html
<script>
function getParameterByName(name, def) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? def : decodeURIComponent(results[1].replace(/\+/g, " "));
}
function someReplacements(text) {
  text = text.replace(/\(!\)/g, '<i class="fa fa-exclamation-triangle" style="color:#C7254E;"> </i> ');
  text = text.replace(/(\-)+&gt;/g, '<i class="fa fa-long-arrow-right"> </i>');
  text = text.replace(/:fa\-([^:]+):/g, '<i class="fa fa-$1"> </i>');
  return text;
}
marked.setOptions({
  renderer: new marked.Renderer(),
  sanitize: false,
  smartypants: true
});
$(document).ready(function() {$("#content").load(getParameterByName('p', 'home')+'.md',function(){$("#content").html(marked(someReplacements($("#content").html())));$('pre code').each(function(i, block) {hljs.highlightBlock(block);});});});
</script>
````


# Canvas

## Fabricjs

* http://fabricjs.com/
* https://www.sitepoint.com/introduction-to-fabric-js/
* http://fabricjs.com/kitchensink
* https://www.eraseimage.com/


# Icons & co

* http://loading.io/
* http://app.fontastic.me/#select/5kBxqLMsLKHCtgoBPxWvWS
* font-awesome


# Databases

* https://www.quora.com/Which-database-should-I-use-for-a-killer-web-application-MongoDB-PostgreSQL-or-MySQL


## MongoDB

* https://www.mongodb.com/fr
* https://openclassrooms.com/courses/guide-de-demarrage-pour-utiliser-mongodb
* https://api.mongodb.com/python/current/
* https://pypi.python.org/pypi/pymongo
* http://www.mongodbspain.com/en/2014/03/23/mongodb-cheat-sheet-quick-reference/
* https://blog.codecentric.de/files/2012/12/MongoDB-CheatSheet-v1_0.pdf


````
/home/bluche/src/mongodb-linux-x86_64-2.6.10/bin/mongodump --host asterion:28283 
/home/bluche/src/mongodb-linux-x86_64-2.6.10/bin/mongorestore --host asterion:28283 dump/
````

* http://edgytech.com/umongo/ - GUI interface

## PostgreSQL

* psycopg - http://initd.org/psycopg/docs/index.html
* https://www.fullstackpython.com/postgresql.html
* https://blog.heapanalytics.com/when-to-avoid-jsonb-in-a-postgresql-schema/
* Async - https://github.com/aio-libs/aiopg

## Misc.

* ``python-sql``


# Python servers

## Misc.

* [Python in the web](https://docs.python.org/2/howto/webservers.html)
* [Build a web app fast: Python, HTML & JavaScript resources](http://www.pixelmonkey.org/2012/06/14/web-app)
* [WSGI servers](https://www.fullstackpython.com/wsgi-servers.html)
* [Gandi hosting](https://www.gandi.net/hosting/)


## bottle

* https://bottlepy.org/docs/dev/
* https://github.com/bottlepy/bottle
* http://sametmax.com/creer-un-site-avec-bottle-en-5-minutes-parceque-7-cest-impossible-voyons/


:warning: bottle is not multithreaded! https://bottlepy.org/docs/dev/deployment.html

## CherryPy

http://cherrypy.org/


## tornado 

http://www.tornadoweb.org/en/stable/

* on multithreading - https://groups.google.com/forum/#!topic/python-tornado/F2oOrffXxOM

## django

https://www.djangoproject.com/


## paste

https://bitbucket.org/ianb/paste/


# Long process in web servers

* yield and callback functions - https://codereview.stackexchange.com/questions/31789/progress-report-for-a-long-running-process-using-yield

* [REST and long-running jobs](http://farazdagi.com/blog/2014/rest-long-running-jobs/)

* [Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)
  * [...and Flask](https://github.com/ask/flask-celery/)

## Sockets

* [Full Stack Python](https://www.fullstackpython.com/websockets.html)
* [WebSuckets](http://lanyrd.com/2013/realtime-conf-europe/sccpxf/)
* [Processing long-running Django tasks using Celery + RabbitMQ + Supervisord + Monit](https://hiddentao.com/archives/2012/01/27/processing-long-running-django-tasks-using-celery-rabbitmq-supervisord-monit/)
* [Mongo and Websockets for application logging](http://feathj.com/2013/08/01/mongo-and-websockets-for-application-logging/)


* [RabbitMQ](https://www.rabbitmq.com/)


### Tornado and Sockets

* [Realtime web application with Tornado and WebSocket ](http://en.proft.me/2014/05/16/realtime-web-application-tornado-and-websocket/)

## async

* explanation - http://mathieu.agopian.info/blog/python-et-asyncio-la-recette-du-bonheur.html
* async with tornado - https://gist.github.com/lbolla/3826189

## Realtime

* [Lessons Learned Architecting Realtime Applications](https://lincolnloop.com/blog/architecting-realtime-applications/)
* [Python and Real-time web](http://mrjoes.github.io/2013/06/21/python-realtime.html)
* [Stateless and Proud in the Realtime World](http://lucumr.pocoo.org/2012/8/5/stateless-and-proud/)

# Editors

* Atom : https://github.com/atom/atom/blob/master/docs/build-instructions/linux.md


# MOOCs

* https://www.coursera.org/learn/web-app#syllabus
* https://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django
* https://www.udacity.com/course/web-development--cs253


# Misc. python

* https://awesome-python.com/



