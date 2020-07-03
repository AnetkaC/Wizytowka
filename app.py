from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)


# funkcja wyświetli dane o mnie
@app.route('/o_mnie')
def o_mnie():
    return render_template('o_mnie.html')




# # funkcja wyświetli dane kontaktowe, dodatkowo dlatego skomentowane
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')



# funkcja wpisze wszystkie parametry zapisane z formularza kontakt

@app.route('/contact', methods=['GET', 'POST'])
def contact() -> str:
    if request.method =='GET':
        print("We received GET")
        return render_template("contact.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form_kontakt)
        return redirect("/")

if __name__ == "__main__":
    app.run()