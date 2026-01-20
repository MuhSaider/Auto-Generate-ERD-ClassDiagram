from flask import Flask, render_template, request, send_file
import os
# Mengimpor fungsi utama dari script yang sudah kamu buat
from auto_drawio import generate_drawio_final_fixed
from auto_classdiagram_drawio import generate_class_diagram_final_v6

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sql_content = request.form.get('sql_content')
        
        if sql_content:
            # 1. Simpan input ke database.sql sementara
            with open('database.sql', 'w', encoding='utf-8') as f:
                f.write(sql_content)
            
            # 2. Jalankan fungsi dari script kamu tanpa mengubah isinya
            erd_file = os.path.join(UPLOAD_FOLDER, 'auto_drawio.drawio')
            class_file = os.path.join(UPLOAD_FOLDER, 'auto_classdiagram_drawio.drawio')
            
            generate_drawio_final_fixed('database.sql', erd_file)
            generate_class_diagram_final_v6('database.sql', class_file)
            
            return render_template('index.html', success=True, erd=erd_file, class_diag=class_file)
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)