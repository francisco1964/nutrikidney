# @app.route('/equivalentes', methods = ["GET", "POST"])
# def get_equivalentes():
#     link_nuevo = url_for("nuevo_equivalente")
#     form = SearchForm()
#     equivalentes = []
#     if form.validate_on_submit():
#         with app.app_context():
#             equivalentes = db.session.query(Equivalente).filter(Equivalente.nombre.contains(form.texto.data)).all()
#             for equivalente in equivalentes:
#                 print(equivalente.nombre, \
#                 equivalente.propiedades[0].valor,\
#                 equivalente.propiedades[1].valor)
#                 for prop in equivalente.propiedades:
#                     # print(prop.concepto.nombre, prop.valor)
#                     pass

from flask import render_template, url_for, redirect
from app.equivalentes import bp
from forms import SearchForm, NewEquivalenteForm, EditPropiedadForm

from app.extensions import db
from app.models.equivalente import Equivalente
from app.models.propiedad import Propiedad
from app.models.concepto import Concepto
from app.models.grupo import Grupo


@bp.route('/',methods = ["GET","POST"])
def index():
    # equivalentes = Equivalente.query.all()
    link_nuevo = url_for("equivalentes.nuevo_equivalente")
    form = SearchForm()
    equivalentes = []

    if form.validate_on_submit():
        equivalentes = Equivalente.query.\
            filter(Equivalente.nombre.contains(form.texto.data)).\
            all()

    # return render_template('equivalentes/index.html', form = form, equivalentes = equivalentes)
    return render_template("equivalentes/index.html",form=form, \
                           equivalentes = equivalentes,\
                            nuevo = link_nuevo)


@bp.route("/equivalente/<int:index>", methods=["GET", "POST"] )
def show_equivalente(index):
    link_nuevo = url_for("equivalentes.nuevo_equivalente")
    eq = None
    # with bp.app_context():
    #     eq = db.session.query(Equivalente).filter(Equivalente.id==index).first()
    #     return render_template("equivalentes/equivalente.html",equivalente = eq, nuevo=link_nuevo)
    
    eq = Equivalente.query.filter(Equivalente.id==index).first()
    return render_template("equivalentes/equivalente.html",equivalente = eq, nuevo=link_nuevo)
    # return redirect(url_for("equivalentes.get_equivalentes"))



@bp.route("/nuevo_equivalente", methods = ["GET","POST"] )
def nuevo_equivalente():
    # return "Nuevo Equivalente"
    link_nuevo = url_for("equivalentes.nuevo_equivalente")
    form = NewEquivalenteForm()

    if form.validate_on_submit():
        print(form.grupo.data) 
        grupo_id = form.grupo.data
        new_equivalente = Equivalente(grupo_id = form.grupo.data,\
                                      nombre = form.nombre.data)
        # IMPORTANTE:se supone que se ha cargado la base con al menos
        # un equivalente de cada grupo, con todo y sus propiedades.
        conceptos = db.session.query(Concepto)\
        .join(Propiedad)\
        .join(Equivalente)\
        .join(Grupo).filter(Grupo.id == form.grupo.data).distinct().all()
        propiedades = [Propiedad(concepto_id = c.id,valor="N.D.") for c in conceptos]
        for p in propiedades:
            new_equivalente.propiedades.append(p)
        db.session.add(new_equivalente)
        for p in propiedades:
            db.session.add(p)
        
        db.session.commit()
        id = new_equivalente.id
        print(f"El id es {id}")

        return redirect(url_for('equivalentes.show_equivalente',index=id))

    # with bp.app_context():
    grupos = db.session.query(Grupo).all()
    form.grupo.choices=[(g.id, g.nombre) for g in grupos ]       

    return render_template("equivalentes/nuevo_equivalente.html",form=form, nuevo = link_nuevo)


@bp.route("/delete_equivalente/<int:index>", methods=["GET", "POST"] )
def delete_equivalente(index):
    # return f"Ediatar Propiedad { index} "
    propiedades = db.session.query(Propiedad).filter(Propiedad.equivalente_id == index).all()
    for p in propiedades:
        db.session.delete(p)
    eq = \
    db.session.query(Equivalente).filter(Equivalente.id == index).first()
    db.session.delete(eq)
    db.session.commit()

    return redirect(url_for('equivalentes.index'))



@bp.route("/edit_prop/<int:index>", methods=["GET", "POST"] )
def edit_prop(index):
    form = EditPropiedadForm()
    prop = None


    if form.validate_on_submit(): 
        prop = db.session.query(Propiedad).filter(Propiedad.id==index).first()  
        db.session.query(Propiedad).filter(Propiedad.id==index).\
        update({'valor' : form.texto.data})
        db.session.commit()
        return redirect(url_for('equivalentes.show_equivalente',index=prop.equivalente.id))

    prop = db.session.query(Propiedad).filter(Propiedad.id==index).first()
    form.texto.data = prop.valor 


    return render_template("equivalentes/edit_prop.html",form=form, prop = prop)



# @bp.route('/categories/')
# def categories():
#     return render_template('posts/categories.html')


