class Ricecooker:
  jumlah = 0
  def __init__(self,nama_merk,tuas,mode): 
    self.nama_merk = nama_merk
    self.tuas = tuas 
    self.mode = mode
    Ricecooker.jumlah += 1
    print('Mode ricecooker :' + self.mode)
ricecooker = Ricecooker('YoungMa', 'ON', 'Cook')
print(ricecooker.nama_merk)

while True:
  try:
    temperature = int(input('Silahkan masukan temperature : '))
    settemperature = int(input('Silahkan set temperature : '))
    newtemperature = temperature + settemperature
    break
  except:
    print('temperature error')
print('Temperature berhasil diubah, temperature sekarang adalah : ', newtemperature)
