
from flask import render_template, url_for, redirect
from app.recetas import bp
from app.recetas.forms import SearchForm, NewRecetaForm


from app.extensions import db
# from app.models.receta import Receta
from app.models.propiedad import Propiedad
# from app.models.concepto import Concepto
# from app.models.grupo import Grupo


@bp.route('/',methods = ["GET","POST"])
def index():
    # recetas = Receta.query.all()
    link_nuevo = url_for("recetas.nuevo_receta") #cambiar a receta
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



@bp.route("/nuevo_receta", methods = ["GET","POST"] )
def nuevo_receta():
    # return "Nuevo Receta"
    link_nuevo = url_for("recetas.nuevo_receta")
    form = NewRecetaForm()

    if form.validate_on_submit():
        

        # return redirect(url_for('recetas.show_receta',index=id))
        pass

    # with bp.app_context():
    # grupos = db.session.query(Grupo).all()
    # unidades = Propiedad.query.filter(Propiedad.concepto_id==2).distinct()
    unidades = Propiedad.query.filter(Propiedad.concepto_id ==2).group_by(Propiedad.valor).\
    order_by(Propiedad.valor)
    form.unidad.choices=[(u.id, u.valor) for u in unidades ]       

    return render_template("recetas/nuevo_receta.html",form=form, nuevo = link_nuevo)
