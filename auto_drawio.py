import re
from xml.dom import minidom

def generate_drawio_final_fixed(sql_file, output_file):
    doc = minidom.Document()
    mxfile = doc.createElement('mxfile')
    mxfile.setAttribute('host', 'Electron')
    doc.appendChild(mxfile)
    
    diagram = doc.createElement('diagram')
    diagram.setAttribute('id', 'diagram_1')
    diagram.setAttribute('name', 'ERD Chen Fixed')
    mxfile.appendChild(diagram)
    
    mxGraphModel = doc.createElement('mxGraphModel')
    mxGraphModel.setAttribute('dx', '1200')
    mxGraphModel.setAttribute('dy', '1200')
    diagram.appendChild(mxGraphModel)
    
    root = doc.createElement('root')
    mxGraphModel.appendChild(root)
    
    # Layer dasar wajib
    for i in ['0', '1']:
        cell = doc.createElement('mxCell')
        cell.setAttribute('id', i)
        if i == '1': cell.setAttribute('parent', '0')
        root.appendChild(cell)

    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_text = f.read()

    # 1. Ekstrak Entitas (Kotak)
    table_pattern = re.compile(r'CREATE TABLE `(\w+)` \((.*?)\) ENGINE', re.S | re.I)
    tables = table_pattern.findall(sql_text)

    id_cnt = 10 
    y_pos = 100
    node_map = {}

    for table_name, body in tables:
        t_id = str(id_cnt)
        node_map[table_name] = t_id
        
        # Entitas
        mxp = doc.createElement('mxCell')
        mxp.setAttribute('id', t_id)
        mxp.setAttribute('value', table_name.upper())
        mxp.setAttribute('style', 'rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#666666;fontStyle=1')
        mxp.setAttribute('parent', '1')
        mxp.setAttribute('vertex', '1')
        
        geo = doc.createElement('mxGeometry')
        geo.setAttribute('x', '500')
        geo.setAttribute('y', str(y_pos))
        geo.setAttribute('width', '140')
        geo.setAttribute('height', '60')
        geo.setAttribute('as', 'geometry')
        mxp.appendChild(geo)
        root.appendChild(mxp)
        id_cnt += 1

        # 2. Ekstrak Atribut (Oval)
        columns = re.findall(r'^\s*`(\w+)`', body, re.M)
        x_attr = 50
        for col in columns:
            if col.upper() in ['KEY', 'PRIMARY', 'UNIQUE', 'CONSTRAINT']: continue
            
            a_id = str(id_cnt)
            mxa = doc.createElement('mxCell')
            mxa.setAttribute('id', a_id)
            mxa.setAttribute('value', col)
            mxa.setAttribute('style', 'ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;')
            mxa.setAttribute('parent', '1')
            mxa.setAttribute('vertex', '1')
            
            ageo = doc.createElement('mxGeometry')
            ageo.setAttribute('x', str(x_attr))
            ageo.setAttribute('y', str(y_pos))
            ageo.setAttribute('width', '90')
            ageo.setAttribute('height', '45')
            ageo.setAttribute('as', 'geometry')
            mxa.appendChild(ageo)
            root.appendChild(mxa)
            
            # GARIS HUBUNG ATRIBUT (PENTING: Menambahkan mxGeometry)
            edge = doc.createElement('mxCell')
            edge.setAttribute('id', str(id_cnt + 1))
            edge.setAttribute('parent', '1')
            edge.setAttribute('source', a_id)
            edge.setAttribute('target', t_id)
            edge.setAttribute('edge', '1')
            edge.setAttribute('style', 'endArrow=none;html=1;rounded=0;')
            
            eg = doc.createElement('mxGeometry')
            eg.setAttribute('relative', '1')
            eg.setAttribute('as', 'geometry')
            edge.appendChild(eg)
            root.appendChild(edge)
            
            id_cnt += 2
            x_attr += 120
            if x_attr > 400: x_attr = 50; y_pos += 80
        
        y_pos += 300

    # 3. Ekstrak Relasi & Kardinalitas (Belah Ketupat)
    fk_pattern = re.compile(
        r'ALTER TABLE `(\w+)`.*?ADD CONSTRAINT `.*?` FOREIGN KEY \(`(.*?)`\) REFERENCES `(\w+)` \(`(.*?)`\)', 
        re.S | re.I
    )
    
    relations = fk_pattern.findall(sql_text)
    rel_y = 200
    for source_table, source_col, target_table, target_col in relations:
        if source_table in node_map and target_table in node_map:
            rel_id = str(id_cnt)
            
            # Simbol Relasi
            mxr = doc.createElement('mxCell')
            mxr.setAttribute('id', rel_id)
            mxr.setAttribute('value', 'Memiliki')
            mxr.setAttribute('style', 'rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;')
            mxr.setAttribute('parent', '1')
            mxr.setAttribute('vertex', '1')
            
            rgeo = doc.createElement('mxGeometry')
            rgeo.setAttribute('x', '520')
            rgeo.setAttribute('y', str(rel_y))
            rgeo.setAttribute('width', '100')
            rgeo.setAttribute('height', '60')
            rgeo.setAttribute('as', 'geometry')
            mxr.appendChild(rgeo)
            root.appendChild(mxr)
            
            # GARIS RELASI N (Menambahkan mxGeometry)
            e1 = doc.createElement('mxCell')
            e1.setAttribute('id', str(id_cnt + 1))
            e1.setAttribute('value', 'N')
            e1.setAttribute('style', 'endArrow=none;html=1;rounded=0;labelBackgroundColor=#ffffff;')
            e1.setAttribute('parent', '1')
            e1.setAttribute('source', node_map[source_table])
            e1.setAttribute('target', rel_id)
            e1.setAttribute('edge', '1')
            
            eg1 = doc.createElement('mxGeometry')
            eg1.setAttribute('relative', '1')
            eg1.setAttribute('as', 'geometry')
            e1.appendChild(eg1)
            root.appendChild(e1)
            
            # GARIS RELASI 1 (Menambahkan mxGeometry)
            e2 = doc.createElement('mxCell')
            e2.setAttribute('id', str(id_cnt + 2))
            e2.setAttribute('value', '1')
            e2.setAttribute('style', 'endArrow=none;html=1;rounded=0;labelBackgroundColor=#ffffff;')
            e2.setAttribute('parent', '1')
            e2.setAttribute('source', rel_id)
            e2.setAttribute('target', node_map[target_table])
            e2.setAttribute('edge', '1')
            
            eg2 = doc.createElement('mxGeometry')
            eg2.setAttribute('relative', '1')
            eg2.setAttribute('as', 'geometry')
            e2.appendChild(eg2)
            root.appendChild(e2)
            
            id_cnt += 3
            rel_y += 350

    xml_str = doc.toprettyxml(indent="  ")
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(xml_str)
    
    print(f"File berhasil dibuat: {output_file}")

if __name__ == "__main__":
    generate_drawio_final_fixed('database.sql', 'erd_final_fix.drawio')