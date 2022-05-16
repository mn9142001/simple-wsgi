from pathlib import Path

#pip install jinja2
from jinja2 import Environment, FileSystemLoader

current_directory = Path(__file__).resolve().parent

#set the template folder for jinja
env = Environment(loader=FileSystemLoader(current_directory))

def render_template(filename, context=None):
    #get template
    template = env.get_template(filename)
    
    #render template
    return template.render(
        {
            "rendered" : context
        }
    )

def server(request, start_response):
    #tell browser your request is successful and the response is html so it can be rendered in clientside
    start_response("200 OK", [('Content-Type', 'text/html; charset=utf-8')])
    #the data returned in response.body in this case the template code
    #index.html is your html template, make one
    return [bytes(render_template('index.html'), encoding='utf-8')]

#code to be executed on typing python filename.py
if __name__ == '__main__':
    #import server
    #pip install waitress
    from waitress import serve
    #run server with port 5000, check http://localhost:5000
    serve(server, port=5000)
