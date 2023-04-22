
from flask import render_template, url_for, redirect
from app.recetas import bp
from app.recetas.forms import SearchForm, NewRecetaForm


from app.extensions import db
# from app.models.receta import Receta
# from app.models.propiedad import Propiedad
# from app.models.concepto import Concepto
# from app.models.grupo import Grupo


@bp.route('/',methods = ["GET","POST"])
def index():
    # recetas = Receta.query.all()
    link_nuevo = url_for("equivalentes.nuevo_equivalente") #cambiar a receta
    form = SearchForm()
    recetas = []

    if form.validate_on_submit():
        # recetas = Receta.query.\
        #     filter(Receta.nombre.contains(form.texto.data)).\
        #     all()
        pass
    # return render_template('recetas/index.html', form = form, recetas = recetas)
    return render_template("recetas/index.html",form=form, \
                           recetas = recetas,\
                            nuevo = link_nuevo)
