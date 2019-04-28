# pandas dan numpy wajib buat olah data
import pandas as pd

# CountVectorizer untuk merepresentasikan text sebagai vector
from sklearn.feature_extraction.text import CountVectorizer

# cosine_similarity untuk mencari kesamaan konten
from sklearn.metrics.pairwise import cosine_similarity

print('PROGRAM REKOMENDASI FILM v0.1')
print('-------------------------')
print('''
     _________________
    |,-----------.   /|
    ||           |= | |
    ||  NETFLIX  || | |
    ||       . _o|  | |  __
    |`-----------'  | / /~/
     ~~~~~~~~~~~~~~~~  / /
                       ~~
    	Author		: Anggoro Dhanumurti
    	Email 		: dhanumurtianggoro@gmail.com
..::| Final Project Implementasi Machine Learning Hacktiv8 2019 |::..
''')

# Step 1: Membaca dataset file CSV dan meformat text
df = pd.read_csv('movie_dataset.csv')
df['title'] = df['title'].str.lower()

# Step 2: Membuat fungsi pencarian judul film
def cari_judul_dari_index(index):
	return df[df.index == index]["title"].values[0].title()

def cari_index_dari_judul(title):
	return df[df.title == title]["index"].values[0]

# Step 3: Menyeleksi kolom kategori pada datasets
kolom = ['keywords', 'cast', 'genres', 'director']

# Step 4: Membuat kolom baru berisi kategori diatas
for items in kolom:
	df[items] = df[items].fillna('')

def merge_kolom(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print("Error:", row)

df["merge_kolom"] = df.apply(merge_kolom, axis=1)

# Step 5: Perhitungan matrix dari kolom baru yg dikombinasikan diatas
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["merge_kolom"])

# Step 6: Mencari kesamaan konten dengan cosine_similarity
cosine_sim = cosine_similarity(count_matrix)

# Step 7: Error handling jika film yg dicari gak ada di datasets
try:
	film_user = input("Mau nonton film apa ? ")
	film_user_low = str.lower(film_user)
	film_user_cap = str.capitalize(film_user)

	# Step 8: Cari index film yg mau ditonton
	index_film = cari_index_dari_judul(film_user_low)
	film_rekomendasi = list(enumerate(cosine_sim[index_film]))

	# Step 9: Sorting film yg memiliki kesamaan
	sorting_rekomendasi_film = sorted(film_rekomendasi, key=lambda x: x[1], reverse=True)

	# Step 10: Tampilkan 5 judul film rekomendasi
	i = 0
	print('Orang yang menonton ' + film_user_cap + ' juga menonton :')
	for element in sorting_rekomendasi_film:
		print(cari_judul_dari_index(element[0]))
		i = i + 1
		if i > 5:
			break
except:
	print("Maaf, Film yg anda cari tidak ada di Database kami, Coba cari judul film lain")

