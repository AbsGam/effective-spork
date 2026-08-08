from templates.data import UserRepository
from flask import Flask, render_template, request, redirect, url_for
from templates.validator import validate

app = Flask(__name__)
repo = UserRepository()

@app.get('/')
def register():
    name = {}
    errors = {}
    return render_template('nakidonchik.html', name=name, errors=errors)


@app.post('/users')
def create_users():
    name = {'name': request.form.get('name', "")}
    errors = validate(name)
    if errors:
        return render_template('nakidonchik.html', errors=errors, name=name['name'])

    repo.save(name)
    return redirect(url_for('main_page', current_user=name['name']))


@app.get('/main/<current_user>')
def main_page(current_user):
    all_users = repo.get_all()
    return render_template('index.html', users=all_users, current_user=current_user)

@app.get('/prikol/<name>')
def cow_moo(name):
    return render_template('korova.html', name=name)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
