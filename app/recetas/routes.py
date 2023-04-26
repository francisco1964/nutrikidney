
from flask import render_template, url_for, redirect
from app.recetas import bp
from app.recetas.forms import SearchForm, NewRecetaForm, NewIngredienteForm


from app.extensions import db
# from app.models.receta import Receta
from app.models.propiedad import Propiedad
from app.models.equivalente import Equivalente
# from app.models.grupo import Grupo
from app.models.receta import Receta, Ingrediente

@bp.route('/',methods = ["GET","POST"])
def index():
    # recetas = Receta.query.all()
    link_nuevo = url_for("recetas.nuevo_receta") #cambiar a receta
    form = SearchForm()
    recetas = []

    if form.validate_on_submit():
        recetas = Receta.query.\
            filter(Receta.nombre.contains(form.texto.data)).\
            all()
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
        print("Creando la nueva receta")
        nueva_receta = Receta(nombre = form.nombre.data,\
                              rendimiento = form.rendimiento.data,\
                              unidad = form.unidad.data,\
                              indicaciones = form.indicaciones.data)
        print(form.unidad.data)
        db.session.add(nueva_receta)    
        db.session.commit()
        print(nueva_receta.id)
        return redirect(url_for('recetas.show_receta',index=nueva_receta.id))

    # with bp.app_context():
    # grupos = db.session.query(Grupo).all()
    # unidades = Propiedad.query.filter(Propiedad.concepto_id==2).distinct()
    unidades = Propiedad.query.filter(Propiedad.concepto_id ==2).group_by(Propiedad.valor).\
    order_by(Propiedad.valor)
    form.unidad.choices=[u.valor for u in unidades ]       

    return render_template("recetas/nuevo_receta.html",form=form, nuevo = link_nuevo)



@bp.route("/receta/<index>", methods=["GET", "POST"] )
def show_receta(index):
    link_nuevo = url_for("recetas.nuevo_receta")
    rcta = None
    # with bp.app_context():
    #     eq = db.session.query(Receta).filter(Receta.id==index).first()
    #     return render_template("recetas/receta.html",receta = eq, nuevo=link_nuevo)
    
    rcta = Receta.query.filter(Receta.id==index).first()
    return render_template("recetas/receta.html",receta = rcta, nuevo=link_nuevo)
    # return redirect(url_for("recetas.get_recetas"))

@bp.route("/delete_ingrediente/<int:index>", methods=["GET", "POST"])
def delete_ingrediente(index):
    # return f"Ediatar Propiedad { index} "

    ingrediente = \
        db.session.query(Ingrediente).filter(Ingrediente.id == index).first()
    receta_id = ingrediente.receta_id
    db.session.delete(ingrediente)
    db.session.commit()

    return redirect(url_for('recetas.show_receta',index = receta_id))

@bp.route("/nuevo_ingrediente/<index>/<is_equivalente>", methods = ["GET","POST"] )
def nuevo_ingrediente(index,is_equivalente):
    # return "Nuevo Receta"
    link_nuevo = url_for("recetas.nuevo_receta")
    form = NewIngredienteForm()

    if form.validate_on_submit():
        pass
        ing = None
        eq = None
        if is_equivalente == "1":
            eq = form.ingrediente.data
        else:
            ing = form.ingrediente.data
        nuevo_ingrediente = Ingrediente(receta_id = index,\
                                        cantidad = form.cantidad.data,\
                                        componente_id=ing,\
                                        equivalente_id = eq)        
        db.session.add(nuevo_ingrediente)
        db.session.commit()
        return redirect(url_for("recetas.show_receta",index=index))

        # return redirect(url_for('recetas.show_receta',index=index))

    # with bp.app_context():
    # grupos = db.session.query(Grupo).all()

    # unidades = Propiedad.query.filter(Propiedad.concepto_id==2).distinct()
    if is_equivalente == "1":
        equivs = Equivalente.query.all()
        form.ingrediente.choices = [(e.id, f"{e.nombre}({ e.propiedades[1].valor })") for e in equivs]
    else:
        rcts = Receta.query.all()
        form.ingrediente.choices = [(r.id, f"{r.nombre}({ r.unidad })") for r in rcts]

    return render_template("recetas/nuevo_receta.html",form=form, nuevo = link_nuevo)

@bp.route("/edit_ingrediente/<index>", methods = ["GET","POST"] )
def edit_ingrediente(index):
    # return "Nuevo Receta"
    link_nuevo = url_for("recetas.nuevo_receta")
    form = NewIngredienteForm()

    ingrediente = Ingrediente.query.filter(Ingrediente.id == index).first()
    
    is_equivalente = "1"


    if ingrediente.equivalente == None:
        is_equivalente = "0"

    if form.validate_on_submit():
        pass
        ing = None
        eq = None


        if is_equivalente == "1":
            eq = form.ingrediente.data
        else:
            ing = form.ingrediente.data
        # db.session.add(nuevo_ingrediente)
        # db.session.commit()

        db.session.query(Ingrediente).filter(Ingrediente.id == index).\
            update({'cantidad' : form.cantidad.data,\
                    'equivalente_id': eq,\
                        'componente_id': ing})

        db.session.commit()
        index = ingrediente.receta_id 
        return redirect(url_for("recetas.show_receta",index=index))

        # return redirect(url_for('recetas.show_receta',index=index))

    # with bp.app_context():
    # grupos = db.session.query(Grupo).all()
    # unidades = Propiedad.query.filter(Propiedad.concepto_id==2).distinct()
    form.cantidad.data = ingrediente.cantidad

    if is_equivalente == "1":
        equivs = Equivalente.query.all()
        form.ingrediente.choices = [(e.id, f"{e.nombre}({ e.propiedades[1].valor })") for e in equivs]
        form.ingrediente.data = ingrediente.equivalente_id
    else:
        rcts = Receta.query.all()
        form.ingrediente.choices = [(r.id, f"{r.nombre}({ r.unidad })") for r in rcts]
        form.ingrediente.data = ingrediente.componente_id
    return render_template("recetas/nuevo_receta.html",form=form, nuevo = link_nuevo)




@bp.route("/delete_receta/<int:index>", methods=["GET", "POST"])
def delete_receta(index):
    # return f"Ediatar Propiedad { index} "
    as_ingredient = db.session.query(Ingrediente).filter(
        Ingrediente.componente_id == index).all()
    for i in as_ingredient:
        db.session.delete(i)
    rcta = \
        db.session.query(Receta).filter(Receta.id == index).first()
    db.session.delete(rcta)
    db.session.commit()

    return redirect(url_for('recetas.index'))


