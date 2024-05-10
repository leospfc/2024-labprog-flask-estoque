from flask import Blueprint, render_template

from src.models.categoria import Categoria
from src.modules import db
import sqlalchemy as sa

bp = Blueprint('categoria', __name__, url_prefix='/categoria')


@bp.route('/', methods=['GET', ])
def lista():
    setenca = sa.select(Categoria).order_by(Categoria.nome)
    rset = db.session.execute(setenca).scalars()

    return render_template('categoria/lista.jinja2',
                           rset=rset)
