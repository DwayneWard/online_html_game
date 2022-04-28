from flask import Flask, render_template, request, redirect, url_for

from arena import Arena
from equipment import Equipment
from hero_classes import unit_classes
from unit import PlayerUnit, EnemyUnit
from utils import get_data_for_choosing, get_unit_from_form

app = Flask(__name__)

heroes = {}

arena = Arena()


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/choose-hero/', methods=["GET", "POST"])
def chose_hero():
    if request.method == 'GET':
        return render_template(
            'hero_choosing.html',
            result=get_data_for_choosing(hero=True)
        )
    if request.method == "POST":
        # name = request.form['name']
        # armor_name = request.form['armor']
        # weapon_name = request.form['weapon']
        # unit_class = request.form['unit_class']
        # player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class))
        # player.equip_weapon(Equipment().get_weapon(weapon_name))
        # player.equip_armor(Equipment().get_armor(armor_name))
        player = get_unit_from_form(hero=True)
        heroes['player'] = player
        return redirect(url_for('choose_enemy'))


@app.route('/choose-enemy/', methods=["GET", "POST"])
def choose_enemy():
    if request.method == "GET":
        return render_template('hero_choosing.html',
            result=get_data_for_choosing())
    if request.method == "POST":
        enemy = get_unit_from_form()
        return redirect(url_for("start_fight"))


@app.route('/start_fight/')
def start_fight():
    pass


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
