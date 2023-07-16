import subprocess

#Bu uygulama ile telefonunuzdaki resimler,video vb. bilgisayarınıza aktarabilirsiniz.
#www.ebubekirbastama.com
#www.ebubekirbastama.com.tr
#www.csharpegitimi.com.tr
def transfer_images(source_path, destination_path):
    # ADB komutunu oluştur
    adb_command = "adb pull {source_path} {destination_path}"
    
    # ADB komutunu çalıştır
    result = subprocess.run(adb_command.split(), capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Resimler başarıyla indirildi.")
    else:
        print("Resimleri indirme işlemi başarısız oldu.")
        print("Hata Mesajı:", result.stderr)

# Kullanıcıdan kaynak ve hedef yollarını al
source_path = input("Resimlerin kaydedildiği yol (örn: /sdcard/DCIM/Camera): ")
destination_path = input("Resimlerin indirileceği hedef yol: ")

# Resimleri indir
transfer_images(source_path, destination_path)
