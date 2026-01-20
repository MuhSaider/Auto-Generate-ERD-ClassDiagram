import subprocess
import time

def run_all_scripts():
    # Daftar script yang ingin dijalankan
    scripts = [
        "auto_drawio.py",
        "auto_classdiagram_drawio.py"
    ]
    
    print("="*40)
    print("🚀 MEMULAI GENERATE DIAGRAM")
    print("="*40)

    for script in scripts:
        print(f"⏳ Menjalankan {script}...")
        try:
            # Menjalankan script menggunakan perintah python
            result = subprocess.run(["python", script], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Berhasil: {script}")
            else:
                print(f"❌ Gagal: {script}")
                print(f"Pesan Error:\n{result.stderr}")
        except Exception as e:
            print(f"⚠️ Terjadi kesalahan sistem saat menjalankan {script}: {str(e)}")
        
        time.sleep(1) # Jeda sebentar agar proses tidak bentrok

    print("="*40)
    print("🎉 SELESAI! Periksa folder kamu untuk file .drawio baru.")
    print("="*40)

if __name__ == "__main__":
    run_all_scripts()