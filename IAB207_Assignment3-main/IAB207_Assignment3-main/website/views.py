from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from .models import Event, Order, User
from . import db
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)


@bp.route('/search')
def search():
    if request.args['search']:
        search = '%' + request.args['search'] + '%'
        events = Event.query.filter(Event.event_category.like(search)).all()
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))


@bp.route('/all')
def all():
    return redirect(url_for('main.index'))

@bp.route('/rock')
def rock():
    search = '%' + 'rock' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)

@bp.route('/jazz')
def jazz():
    search = '%' + 'jazz' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)


@bp.route('/electronic music')
def electronic_music():
    search = '%' + 'electronic music' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)


@bp.route('/classical music')
def classical_music():
    search = '%' + 'classical music' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)


@bp.route('/hip-hop')
def hip_hop():
    search = '%' + 'hip-hop' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)


@bp.route('/folk music')
def folk_music():
    search = '%' + 'folk music' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)


@bp.route('/other')
def other():
    search = '%' + 'other' + '%'
    events = Event.query.filter(Event.event_category.like(search)).all()
    return render_template('index.html', events=events)


@bp.route('/history')
@login_required
def history():
    user_id = current_user.id
    order = Order.query.filter(Order.user_id.like(user_id)).all()
    return render_template('history.html', orders=order)


@bp.route('/searchOrder')
def search_order():
    if request.args['search_order']:
        search = '%' + request.args['search_order'] + '%'
        user_id = current_user.id
        order = (
            db.session.query(Order)
            .join(Event)
            .filter(Order.user_id == user_id, Event.event_name.like(search))
            .all()
        )
        return render_template('history.html', orders=order)
    else:
        return redirect(url_for('main.history'))


