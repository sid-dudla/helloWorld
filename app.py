from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Siddharth Dudla! I am adding my first change!'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

@app.route('/update_customer')
def update_customer():
    return render_template('update_customer.html')

@app.route('/favorite-course')
def favorite_course():
    print('You entered your favorite course as: ' + request.args.get('subject') + request.args.get('course_number'))

    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()
