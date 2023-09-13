
# Reservation Cancelation Prediction

Project ini merupakan project mandiri. Project ini memiliki tujuan untuk memanfaatkan Machine Learning guna memprediksi klasisifikasi dari tamu hotel yang mereservasi kamar apakah ia akan mencancel reservasinya atau tidak. Sehingga dapat meminimalisir pengaruh dari adanya cancelation tersebut.

## Deployment Link
Deployment : [https://huggingface.co/spaces/kodokgodog/Credit_Home](https://huggingface.co/spaces/kodokgodog/Hotel_Reservation)

## Permasalahan

Permasalahan yang ada di dalam project ini adalah, diperlukannya pengembangan model klasifikasi dari tamu hotel yang telah melakukan reservasi kepada hotel tersebut membatalkan reservasinya. Hal tersebut dapat berguna untuk manajemen hotel agar bisa melakukan strategi terhadap pembatalan yang akan terjadi. Model ini dibuat dan dilatih yang selanjutnya dilakukan evaluasi dengan menggunakan algoritma machine learning, algoritma yang digunakan dipilih dengan menggunakan metode cross validation dan didapatkan algoritma akhir yang digunakan adalah SVM yang selanjutnya dilakukan hyperparameter tuning menggunakan GridsearchCV. Dengan tujuan untuk memperoleh model yang memiliki kinerja yang paling baik untuk digunakan dalam prediksi. 

## Deskripsi Data

Dataset ini terdiri dari informasi klien pemesan hotel, terutama terkait dengan proses reservasi hotel seperti jumlah tamu, jumlah kamar dipesan, serta kebutuhan khusus lainnya. Variabel target adalah status pembatalan reservasi.

## Evaluasi Model

Model akan dievaluasi berdasarkan kemampuannya dalam mengklasifikasikan pembatalan reservasi dengan benar. Metrik evaluasi utamanya adalah recall, yang memberikan penilaian terhadap kemampuan model dalam membedakan seberapa baik model dalam memprediksi kelas canceled secara akurat.

## Alur Proyek

1. Preproses data: Lakukan pembersihan data, penanganan nilai yang hilang, penanganan outlier, dan pengkodean fitur kategori.
2. Rekayasa fitur: Buat fitur tambahan jika diperlukan dan pilih fitur yang relevan.
3. Pelatihan model: Latih beberapa model pembelajaran mesin termasuk SVM, XGBoost, dan LightGBM.
4. Evaluasi model: Evaluasi model menggunakan berbagai metrik seperti ROC-AUC, akurasi, presisi, dan recall.
5. Hyperparameter Tuning: Dilakukan untuk mengoptimalkan model yang dipilih dengan memilih hiperparameter menggunakan teknik seperti Random Search.
6. Pemilihan model akhir: Memilih model dengan performa terbaik berdasarkan metrik evaluasi.
7. Inferensi model

## Kesimpulan

Kesimpulan EDA:

Distribusi data target adalah 67.2% berbanding 32.8%. Diasumsikan distribusi data tersebut masih balance, karena diasumsikan data yang mulai imbalance adalah data dengan proporsi 70:30.
Berdasarkan jumlah tamu yang mencancel bookingnya terhadap hotel, dapat dilihat bahwa jumlahnya cukup banyak. Hal tersebut dapat membuat kerugian pada hotel apabila tidak ditanggulangi dan diatur dalam sistem booking yang baik.
Room tipe 1 merupakan kamar paling favorit di hotel untuk reservasi. Sebagian besar pelanggan yang mereservasi hotel hanya terdiri dari orang dewasa saja dengan waktu inap yang tidak panjang. Untuk makanan yang mendominasi pada data adalah makanan paket meal_plan_1, dengan mengetahui banyaknya yang memesan makanan ini maka stok makanan ini membutuhkan perhatian khusus agar dapat disesuaikan dengan pemesanan yang akan ada.
Jumlah tamu yang mendominasi di bulan 9 dan 10 serta penurunan tamu pada akhir tahun yaitu di bulan 11 dan 12. Pemesanan hotel didominasi dengan pemesanan online, dengan mengetahui hal ini pihak manajemen dapat memberikan benefit lebih kepada tamu yang memesan online dan juga lebih memerhatikan sistem pemesanan online agar tidak terjadi masalah.

Kesimpulan Model Analysis: 
Berdasarkan Model Analysis yang dibuat diputuskan bahwa SVM merupakan pemodelan model Classification yang terbaik untuk memprediksi tamu yang mencancel reservasi serta didapatkan hal-hal berikut terkait dengan model yang digunakan, yaitu:

1. Evaluasi skor permodelan menggunakan recall, digunakan karena dapat menunjukkan seberapa baik model dalam memprediksi kelas canceled secara akurat.
2.Berdasarkan hasil GridSearcCV maka parameter terbaik yang akan digunakan adalah C = 0.1 dan kernel : rbf. Dengan menggunakan parameter tersebut meningkatkan skor recall yang dihasilkan bila dibandingkan dengan base model.
3.Recall akhir pada data test sebesar 0.9152576899572215 menunjukkan bahwa model mampu mengidentifikasi sekitar 91.52% dari total sampel kelas positif yang sebenarnya. Recall pada data train sebesar 0.9194410193177147 menunjukkan bahwa model mampu mengidentifikasi sekitar 91.94% dari total sampel kelas positif yang sebenarnya.

###Untuk pemodelan yang dilakukan masih dapat ditingkatkan kembali, khususnya dalam pencarian hyperparameter tuningnya, bisa ditingkatkan jumlah iterationya sehingga mungkin dapat tereksplor hyperparameter yang lebih baik lagi dan dapat meningkatkan kinerja model.
