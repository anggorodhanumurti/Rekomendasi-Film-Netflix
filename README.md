# Rekomendasi film menggunakan metode Machine Learning

<p align="center">
 <img src="http://www.codeheroku.com/static/blog/images/pid14_results.png">
</p>

Penasaran bagaimana Google atau situs streaming seperti Netflix menampilkan Rekomendasi film 
sesuai dengan selera kita?

Jawabanya adalah Machine Learning yaitu kemampuan program dalam mengambil keputusan sesuai dengan data aktual yg telah diproses 
sedemikian rupa sehingga menghasilkan prediksi yang akurat.

Program ini dibuat sebagai final project dari training saya di [hacktiv8 - intro to Python for data science](https://hacktiv8.com/python/jakarta/)

## Tutorial

- Saya menggunakan **Python 3** jadi pastikan kamu menggunakan versi python yang sesuai

- Install modul yang dibutuhkan untuk Machine Learning pada program ini saya menggunakan **[pandas](https://pandas.pydata.org/)** dan **[scikit-learn](https://scikit-learn.org/)**

- Siapkan datasets untuk diolah bisa didapatkan di [kaggle.com](https://www.kaggle.com/netflix-inc/netflix-prize-data) datasets yang saya gunakan adalah [`movie_dataset.csv`](https://github.com/anggorodhanumurti/Rekomendasi-Film-Netflix/raw/master/movie_dataset.csv)

- Karena system rekomendasi yang saya buat berbasis konten maka saya menggunakan fungsi cosine similarity. Kode nya bisa dilihat [`disini`](https://github.com/anggorodhanumurti/Rekomendasi-Film-Netflix/blob/master/cosine_similarity.py).

- Main application nya adalah file ['rekomendasi_film.py'](https://github.com/anggorodhanumurti/Rekomendasi-Film-Netflix/blob/master/rekomendasi_film.py) jadi untuk menjalankan program cukup ketik **python rekomendasi_film.py** pada Terminal/CMD

### Refferensi

- [Building Movie Recommender System in Python by CodeHeroku](https://www.youtube.com/watch?v=XoTwndOgXBM "Building Movie Recommender System in Python by CodeHeroku")

- [Kaggle Netflix Datasets](https://www.kaggle.com/netflix-inc/netflix-prize-data "Kaggle Netflix Datasets")

<p align="center"><a href="https://hacktiv8.com/verify/pytn/anggoro-dhanumurti/">
 <img src="https://raw.githubusercontent.com/anggorodhanumurti/Rekomendasi-Film-Netflix/master/IMG_20190615_142521.jpg"></a>
</p>
