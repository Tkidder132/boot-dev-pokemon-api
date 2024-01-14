import sqlite3;
import pandas as pd;

df = pd.read_csv('pokemon.csv');
conn = sqlite3.connect('pokemon.db');
cursor = conn.cursor();
conn.execute("DROP TABLE IF EXISTS POKEMON"); 

create_table_query = '''
CREATE TABLE IF NOT EXISTS Pokemon (
    PK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ID INT,
    Name TEXT,
    Form TEXT,
    Type1 TEXT,
    Type2 TEXT,
    Total INT,
    HP INT,
    Attack INT,
    Defense INT,
    "Sp. Atk" INT,
    "Sp. Def" INT,
    Speed INT,
    Generation INT
);
''';

cursor.execute(create_table_query);

for index, row in df.iterrows():
    cursor.execute(
        'INSERT INTO Pokemon (ID, Name, Form, Type1, Type2, Total, HP, Attack, Defense, "Sp. Atk", "Sp. Def", Speed, Generation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (row['ID'], row['Name'], row['Form'], row['Type1'], row['Type2'], row['Total'], row['HP'], row['Attack'],
         row['Defense'], row['Sp. Atk'], row['Sp. Def'], row['Speed'], row['Generation'])
    );
    print(f"{row['ID']}: {row['Name']} has been added to the database");

conn.commit();
conn.close();
print("SQLite database 'pokemon.db' has been created and populated.");