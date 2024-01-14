import sqlite3;
from flask import Flask, jsonify;

app = Flask(__name__);

full_dict = ["PK_ID", "ID", "Name", "Form", "Type1", "Type2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation"];

def dictify(a):
    return [dict(zip(full_dict,vv)) for vv in a];

def execute_sql(statement):
    conn = sqlite3.connect('pokemon.db');
    cursor = conn.cursor();
    cursor.execute(statement);
    output = cursor.fetchall();
    conn.commit();
    conn.close();
    return output;

def get_all():
    return execute_sql('SELECT * FROM POKEMON');

def get_by_id(id):
    return execute_sql(f"SELECT * FROM POKEMON WHERE ID = {id}");

@app.route("/pokemon", methods=["GET"])
def get_pokemon():
    output = get_all();
    return jsonify(dictify(output));

@app.route("/pokemon/<int:id>", methods=["GET"])
def get_pokemon_by_id(id: int):
    output = get_by_id(id);
    if output is None or len(output) == 0:
        return jsonify({"error": "Pokemon does not exist"}), 404;
    return jsonify(dictify(output));

if __name__ == "__main__":
    app.run(port=5000);