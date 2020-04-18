from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = "12345"

#  ключи recaptcha от google
app.config['RECAPTCHA_PUBLIC_KEY'] = "6Ld74-oUAAAAAJC0UOY6PtrOrNcxQ2VQCfGAqBOC"
app.config['RECAPTCHA_PRIVATE_KEY'] = "6Ld74-oUAAAAAD2_Jl2IVKh2uCCI9OPX_7oTdLz4"
app.config['RECAPTCHA_DISABLE'] = True #  будет капча или нет

#  форма с валидацией и капчей или без неё.
#  в новой версии flask-wtf планируется сделать RECAPTCHA_DISABLE красиво
#  из коробки, это временное решение
if app.config['RECAPTCHA_DISABLE'] == True:
    from forms import ContactRecaptchaForm as ContactForm
else:
    from forms import ContactForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    msg = ""
    if request.method == "POST":
        if form.validate_on_submit():
            msg="Успех!"
            #  отправить почту, записать в БД
        else:
            msg="Ошибка валидации"
            #  обработать ошибку

    return render_template("index.html",
                           title="index page",
                           form=form,
                           msg=msg)


if __name__ == '__main__':
    app.run(debug=True)

