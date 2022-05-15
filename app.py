from pathlib import Path
from jinja2 import Environment, FileSystemLoader

current_directory = Path(__file__).resolve().parent
env = Environment(loader=FileSystemLoader(current_directory))

def render_template(filename, context=None):
    return env.get_template(filename).render(
        {
            "rendered" : context
        }
    )

def server(request, start_response):
    start_response("200 OK", [('Content-Type', 'text/html; charset=utf-8')])
    return [bytes(render_template('index.html', request), encoding='utf-8')]
