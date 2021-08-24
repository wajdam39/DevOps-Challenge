from flask import Flask
import socket

app = Flask(__name__)

def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# Some bits of text for the page
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'


# Add a rule for the index page
app.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# Add a rule when the page is accessed with a name appended to the site
# URL
app.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))





print("HELLOO")  
#@app.route('/')
#def hello():
#    hostname = socket.gethostname()
#    return hostname

@app.route('/healthz')
def health():
    return "healthy"

@app.route('/ready')
def ready():
    return "ready"

  
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
    