from flask import*
from models.service import Service
from mlab  import mlab_connect
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service/<int:gender>')
def search(gender):
    filtered_services = Service.objects(gender= gender, occupied = False)
    return render_template('search.html',all_services =Service.objects())

@app.route('/admin')
def admin():
    return render_template('admin.html',services = Service.objects())

@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects().with_id(service_id)
    service.delete()
    return redirect(url_for('admin'))
@app.route('/new_service', methods=["GET", "POST"])
def new_service():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        phone = form["phone"]
        yob = form["yob"]
        gender = form["gender"]
        height = form["height"]
        new_service = Service(name=name,
                              phone = phone,
                              yob = yob,
                              gender = gender,
                              height = height,
                              occupied = False)
        new_service.save()
        flash("da dang ki thanh cong")
        return render_template("new_service.html")
@app.route('/edit/<service_id>', methods = ['GET', 'POST'])
def edit(service_id):
    if request.method == 'GET':
        service = Service.objects().with_id(service_id)
        return render_template('edit.html', service = service)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        phone = form['phone']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        occupied = form['occupied']
        new_service = Service.objects().with_id(service_id)
        new_service.update(name = name)
        new_service.update(phone = phone)
        new_service.update(yob = yob)
        new_service.update(gender = gender)
        new_service.update(height = height)
        new_service.update(occupied = bool(occupied))
        new_service.reload()
        flash("ok")
        return render_template('edit.html', service = new_service)
if __name__ == '__main__':
  app.run(debug=True)
