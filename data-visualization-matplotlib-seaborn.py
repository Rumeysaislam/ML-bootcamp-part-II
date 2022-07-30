# VERI GORSELLESTIRME: MATPLOTLIB & SEABORN

# MATPLOTLIB ;
# low level, veri gorsellestirme aracidir. Yani seaborn'a kiyasla daha fazla caba ile veri gorsellestirme anlamina gelir.


# Kategorik degisken: sutun grafik, countplot bar
# Sayisal degisken: histogram, boxplot (degiskenin dagilimini verirler ama boxplot; aykiri degerleri de verir.)

# (Veri tabanina bagli veri gorsellestirme araclari kullanmak daha avantajlidir.)


# Kategorik Degisken Gorsellestirme;
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)                              # Tum degerleri gormek istiyoruz.
pd.set_option('display.width', 500)                                     # Veriyi yan yana gormek istiyoruz ve sinirladik.
df = sns.load_dataset("titanic")
df.head()

# Cinsiyet kategorik degiskeninin grafigini cizmek istiyorum;
# Value_counts(); önemli
df['sex'].value_counts().plot(kind='bar')                               # Sutun grafik (barplot) olarak; kind='bar'
plt.show()


# matplotlib'i guncellemek istersek; "pip install matplotlib" yaparak bastan kurariz yada
# " pip install -- upgrade matplotlib " yaparak guncelleriz.



# Sayisal Degisken Gorsellestirme;

import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

# histogram ile;
plt.hist(df["age"])
plt.show()

#boxplot (kutu grafik) ile; veri setindeki aykırı degerleri, ceyreklik degerler uzerinden yakaliyor.
plt.boxplot(df["fare"])
plt.show()

# Sayisal degiskenlerin hangi aralikta hangi frekanslarda oldugunu hem de veri setindeki bu degiskenin kendi icindeki dagilim bilgisini
# ve bu dagilima gore ne kadar aykiri deger olacagi bilgisini verir.



# Matplotlib'in Ozellikleri

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)


# plot

# Matplotlib katmanli sekilde veri gorsellestirmemizi saglar.

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

# Cizgisiz sekilde o noktalara sadece nokta koymak istersek;
plt.plot(x, y, 'o')
plt.show()
# Onceki grafik acık kalirsa noktalari cizginin üzerine koyar, yeniden ac.
# Grafikleri acik birakirsan, yenisini ustune atar.

# Daha fazla nokta;
x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()



# Marker ; Isaretleyici Ozellikleri

y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o')
plt.show()

plt.plot(y, marker='*')
plt.show()

# Kullanilabilecek markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']



# Line ; Cizgi Ozelligi

y = np.array([13, 28, 11, 100])
plt.plot(y)
plt.show()


# linestyle="dashed"    : kesikli
# linestyle="dashdot"   : hem nokta hem kesik
# linestyle="dotted"    : noktali

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot")
plt.show()

# Renk ozelligi eklemek istersem;
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot", color="r")
plt.show()



# Multiple Lines ; Coklu Cizgiler

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

# Pes pese gosterirsek, iki veriyi bir arada gorebiliriz. Matplolib'in katmanlı yapisindan dolayı :P



# Labels ; Etiketler

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)

# Baslik;
plt.title("Bu ana baslik")

# X eksenini isimlendirme;
plt.xlabel("X ekseni isimlendirmesi")

plt.ylabel("Y ekseni isimlendirmesi")

plt.grid()              # Izgara ekleyip, okunabilirligi kolaylastirmak icin.
plt.show()



# Subplots; Birden fazla gorselin gosterilmesi calismalari

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)                                                    # 1 satirlik, 2 sutunluk grafigin 1. grafigini olusturuyorum demek.
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)
plt.show()


# 3 grafiği bir satır 3 sütun olarak konumlamak. (Bir satirlik, uc sutunluk grafik)
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)

plt.show()




# SEABORN ; veri gorsellestirmek icin kullanilan; yuksek seviye (daha az cabayla daha cok is) bir kutuphanedir.

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()



# Kategorik Degisken Gorsellestirme;

df["sex"].value_counts()                                                # Cinsiyetlerin dagilim bilgisini cektik.
sns.countplot(x=df["sex"], data=df)                                     # countplot icin "x =..." ; x ekseninde ne olacagini ve "data=df" verinin ne oldugunu bildirmen lazim.
plt.show()

# matplolib'de boyle yapiyorduk;
df['sex'].value_counts().plot(kind='bar')
plt.show()



# Sayisal Degisken Gorsellestirme;

sns.boxplot(x=df["total_bill"])
plt.show()


df["total_bill"].hist()
plt.show()
