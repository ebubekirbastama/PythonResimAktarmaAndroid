import subprocess

#Bu uygulama ile telefonunuzdaki resimler,video vb. bilgisayarınıza aktarabilirsiniz.
#www.ebubekirbastama.com
#www.ebubekirbastama.com.tr
#www.csharpegitimi.com.tr
def transfer_images(source_path, destination_path):
    adb_command = f"adb pull {source_path} {destination_path}"
    
    print(adb_command)
    result = subprocess.run(adb_command.split(), capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Resimler başarıyla indirildi.")
    else:
        print("Resimleri indirme işlemi başarısız oldu.")
        print("Hata Mesajı:", result.stderr)

source_path = str(input("Resimlerin kaydedildiği yol (örn: /sdcard/DCIM/Camera): "))
destination_path = str(input("Resimlerin indirileceği hedef yol: "))

transfer_images(source_path, destination_path)
