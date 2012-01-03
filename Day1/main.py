#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

from random import choice


class MainHandler(webapp.RequestHandler):
    def get(self):
        greetings = ["Hi","Hello"]
        greeting = choice(greetings)    
        self.response.out.write('<html><b>%s, Whoever!</b></html>' % greeting)
        
        self.response.out.write('<html><br></html>')

        suits = ["clubs","hearts","spades","diamonds"]
        cardName = "%s of %s" % (choice(range(1,11)), choice(suits))
        self.response.out.write('<html>%s</html>' % cardName)

        #Using templates
        self.response.out.write(template.render("Templates/index.html", {'cardName' : cardName}))

    def post(self):
        self.response.out.write("That was a post.")


def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ('/submit', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
