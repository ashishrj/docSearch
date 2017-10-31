from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!\n"

@app.route('/hello/<name>')
def hello_world1(name=None):
    #return "HELLO WORLD! Today is {}\n".format(date)
    return render_template('hello.html', name=name)

@app.route('/temp')
def show_template():
    return render_template('layout.html')

@app.route('/search')
def search_in_doc():
    return render_template('search_page.html')

if __name__ == "__main__":
    #app.run()
    pass
