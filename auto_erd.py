import os
import re
from graphviz import Digraph

# Tambahkan Path Graphviz jika belum masuk environment variable
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

def generate_erd_from_phpmyadmin(sql_file):
    dot = Digraph('ERD_Chen_Notasi', format='png')
    dot.attr(rankdir='TB', nodesep='0.8', ranksep='1.2')

    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_text = f.read()

    # 1. Ekstrak Semua Tabel (CREATE TABLE)
    # Regex ini menangani backticks (`) dan spasi ekstra
    table_pattern = re.compile(r'CREATE TABLE `(\w+)` \((.*?)\) ENGINE', re.S | re.I)
    tables = table_pattern.findall(sql_text)

    for table_name, body in tables:
        # Gambar Entitas (Kotak)
        dot.node(table_name, table_name.upper(), shape='box', style='filled', color='lightblue')

        # 2. Ekstrak Kolom/Atribut
        # Mencari kata di awal baris yang diapit backticks
        column_matches = re.findall(r'^\s*`(\w+)`', body, re.M)
        
        for col in column_matches:
            # Skip jika itu kata kunci SQL
            if col.upper() in ['KEY', 'PRIMARY', 'UNIQUE', 'CONSTRAINT']: continue
            
            attr_id = f"{table_name}_{col}"
            # Gambar Atribut (Oval)
            dot.node(attr_id, col, shape='ellipse')
            dot.edge(table_name, attr_id)

    # 3. Ekstrak Relasi dari ALTER TABLE (Foreign Key)
    # phpMyAdmin meletakkan relasi di perintah ALTER TABLE di bagian bawah
    fk_pattern = re.compile(
        r'ALTER TABLE `(\w+)`.*?ADD CONSTRAINT `.*?` FOREIGN KEY \(`.*?`\) REFERENCES `(\w+)` \(`.*?`\)', 
        re.S | re.I
    )
    
    relations = fk_pattern.findall(sql_text)
    for source_table, target_table in relations:
        rel_name = f"rel_{source_table}_{target_table}"
        # Gambar Relasi (Belah Ketupat)
        # Kita gunakan label umum "Memiliki/Relasi"
        dot.node(rel_name, "Relasi", shape='diamond', style='filled', color='yellow')
        dot.edge(source_table, rel_name)
        dot.edge(rel_name, target_table)

    # Render Hasil
    output_file = 'output_erd_absensi'
    dot.render(output_file, view=True)
    print(f"Selesai! File '{output_file}.png' telah dibuat.")

if __name__ == "__main__":
    # Pastikan file SQL kamu dinamai 'database.sql' atau ganti nama di bawah ini
    generate_erd_from_phpmyadmin('database.sql')