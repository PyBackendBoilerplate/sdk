import os

from flask import render_template

from sdk.infra.app.wsgi import create_flask_microservice

microservice, settings = create_flask_microservice()
settings.name = 'Hello Flask'
settings.template_folder = os.path.abspath('./templates')
app = microservice.create_app()


@app.route('/')
def root():
    return "Hello, World!"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(host=settings.host, port=settings.port)
