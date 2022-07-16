from flask import Flask, request, render_template
from os import path

app = Flask(__name__, static_folder='files')


@app.route('/')
def form():
    return render_template(
        'index.html',
        flag=False
    )


@app.route('/get-cert', methods=['POST'])
def get_cert():
    a = 'files/' + ' '.join([x[0].upper() + x[1:].lower() for x in request.form['fio'].split(' ')]) + '.pdf'
    ok = False
    if path.exists(a):
        ok = True
    return render_template(
        'index.html',
        flag=True,
        ok=ok,
        link=a,
        name=' '.join([x[0].upper() + x[1:].lower() for x in request.form['fio'].split(' ')])
    )


def main():
    app.run('127.0.0.1', 80, debug=True)


if __name__ == '__main__':
    main()
