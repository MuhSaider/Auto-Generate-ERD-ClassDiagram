import re
from xml.dom import minidom

def generate_class_diagram_final_v6(sql_file, output_file):
    doc = minidom.Document()
    mxfile = doc.createElement('mxfile')
    mxfile.setAttribute('host', 'Electron')
    doc.appendChild(mxfile)
    
    diagram = doc.createElement('diagram')
    diagram.setAttribute('id', 'diagram_class')
    diagram.setAttribute('name', 'Class Diagram Lengkap')
    mxfile.appendChild(diagram)
    
    mxGraphModel = doc.createElement('mxGraphModel')
    mxGraphModel.setAttribute('dx', '1500')
    mxGraphModel.setAttribute('dy', '1500')
    diagram.appendChild(mxGraphModel)
    
    root = doc.createElement('root')
    mxGraphModel.appendChild(root)
    
    for i in ['0', '1']:
        cell = doc.createElement('mxCell')
        cell.setAttribute('id', i)
        if i == '1': cell.setAttribute('parent', '0')
        root.appendChild(cell)

    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_text = f.read()

    table_pattern = re.compile(r'CREATE TABLE `(\w+)` \((.*?)\) ENGINE', re.S | re.I)
    tables = table_pattern.findall(sql_text)

    id_cnt = 100
    x_pos = 100
    y_pos = 100
    node_map = {}

    for table_name, body in tables:
        class_id = str(id_cnt)
        node_map[table_name] = class_id
        
        # PERBAIKAN REGEX: Menangkap nama kolom dan seluruh tipe datanya hingga koma atau akhir baris
        # Ini akan menangkap "int(11)" atau "enum('A','B')" secara utuh
        columns = re.findall(r'^\s*`(\w+)`?\s+([\w\(\)\',]+)', body, re.M)
        
        h_header = 35
        h_attrs = len(columns) * 22 # Memberi sedikit ruang lebih untuk teks panjang
        h_sep = 8
        h_meths = 70
        total_h = h_header + h_attrs + h_sep + h_meths

        mxc = doc.createElement('mxCell')
        mxc.setAttribute('id', class_id)
        mxc.setAttribute('value', table_name.upper())
        mxc.setAttribute('style', 'swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#e1d5e7;strokeColor=#9673a6;html=1;')
        mxc.setAttribute('parent', '1')
        mxc.setAttribute('vertex', '1')
        
        geo = doc.createElement('mxGeometry')
        geo.setAttribute('x', str(x_pos))
        geo.setAttribute('y', str(y_pos))
        geo.setAttribute('width', '280') # Diperlebar agar tipe data ENUM muat
        geo.setAttribute('height', str(total_h))
        geo.setAttribute('as', 'geometry')
        mxc.appendChild(geo)
        root.appendChild(mxc)
        id_cnt += 1

        current_y = 30
        for col_name, col_type in columns:
            mx_attr = doc.createElement('mxCell')
            mx_attr.setAttribute('id', str(id_cnt))
            # Menghapus koma terakhir jika ada di tipe data enum
            clean_type = col_type.rstrip(',')
            mx_attr.setAttribute('value', f"+ {col_name}: {clean_type}")
            mx_attr.setAttribute('style', 'text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=11;')
            mx_attr.setAttribute('parent', class_id)
            mx_attr.setAttribute('vertex', '1')
            
            ageo = doc.createElement('mxGeometry')
            ageo.setAttribute('y', str(current_y))
            ageo.setAttribute('width', '280')
            ageo.setAttribute('height', '22')
            ageo.setAttribute('as', 'geometry')
            mx_attr.appendChild(ageo)
            root.appendChild(mx_attr)
            id_cnt += 1
            current_y += 22

        mx_sep = doc.createElement('mxCell')
        mx_sep.setAttribute('id', str(id_cnt))
        mx_sep.setAttribute('style', 'line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;whiteSpace=wrap;html=1;')
        mx_sep.setAttribute('parent', class_id)
        mx_sep.setAttribute('vertex', '1')
        
        sgeo = doc.createElement('mxGeometry')
        sgeo.setAttribute('y', str(current_y))
        sgeo.setAttribute('width', '280')
        sgeo.setAttribute('height', '8')
        sgeo.setAttribute('as', 'geometry')
        mx_sep.appendChild(sgeo)
        root.appendChild(mx_sep)
        id_cnt += 1
        current_y += 8

        methods = ["create(): void", "update(): void", "delete(): void"]
        for meth in methods:
            mx_meth = doc.createElement('mxCell')
            mx_meth.setAttribute('id', str(id_cnt))
            mx_meth.setAttribute('value', f"+ {meth}")
            mx_meth.setAttribute('style', 'text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;')
            mx_meth.setAttribute('parent', class_id)
            mx_meth.setAttribute('vertex', '1')
            
            mgeo = doc.createElement('mxGeometry')
            mgeo.setAttribute('y', str(current_y))
            mgeo.setAttribute('width', '280')
            mgeo.setAttribute('height', '20')
            mgeo.setAttribute('as', 'geometry')
            mx_meth.appendChild(mgeo)
            root.appendChild(mx_meth)
            id_cnt += 1
            current_y += 20
        
        x_pos += 400
        if x_pos > 1200:
            x_pos = 100
            y_pos += 600

    # Relasi 
    fk_pattern = re.compile(r'ALTER TABLE `(\w+)`.*?ADD CONSTRAINT `.*?` FOREIGN KEY \(`.*?`\) REFERENCES `(\w+)` \(`.*?`\)', re.S | re.I)
    relations = fk_pattern.findall(sql_text)
    
    for src, target in relations:
        if src in node_map and target in node_map:
            edge = doc.createElement('mxCell')
            edge.setAttribute('id', str(id_cnt))
            edge.setAttribute('value', '1      *')
            edge.setAttribute('style', 'endArrow=open;endFill=0;endSize=12;html=1;rounded=0;edgeStyle=orthogonalEdgeStyle;labelBackgroundColor=#ffffff;')
            edge.setAttribute('parent', '1')
            edge.setAttribute('source', node_map[target])
            edge.setAttribute('target', node_map[src])
            edge.setAttribute('edge', '1')
            
            eg = doc.createElement('mxGeometry')
            eg.setAttribute('relative', '1')
            eg.setAttribute('as', 'geometry')
            edge.appendChild(eg)
            root.appendChild(edge)
            id_cnt += 1

    xml_str = doc.toprettyxml(indent="  ")
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(xml_str)
    
    print(f"Berhasil! File Class Diagram Detail: {output_file}")

if __name__ == "__main__":
    generate_class_diagram_final_v6('database.sql', 'class_diagram_detail.drawio')