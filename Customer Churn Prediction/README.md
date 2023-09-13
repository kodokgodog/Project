
# Customer Churn Prediction

Project ini merupakan project mandiri. Project ini memiliki tujuan mengembangkan model prediksi churn yang kuat dan akurat yang dapat digunakan untuk mengidentifikasi pelanggan yang berisiko churn. Hal ini akan memungkinkan perusahaan untuk mengambil tindakan proaktif, seperti kampanye pemasaran yang ditargetkan, penawaran yang dipersonalisasi, atau peningkatan layanan pelanggan, untuk mempertahankan pelanggan dan mengurangi churn.

## Deployment Link
Deployment : https://huggingface.co/spaces/kodokgodog/Customer_Churn_Prediction

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

Kesimpulan EDA (Exploratory Data Analysis):

1. Jumlah pelanggan yang akan churn lebih tinggi dibandingkan dengan yang tidak churn. Angka-angka ini akan memiliki dampak negatif yang signifikan pada bisnis perusahaan, dengan tingkat churn melebihi setengah dari total pelanggan. Berdasarkan persentase data, distribusi data tampak seimbang.
2. Mayoritas pelanggan yang churn adalah bukan anggota atau memiliki tingkat keanggotaan rendah. Berdasarkan data ini, strategi bisnis dapat dikembangkan. Misalnya, menawarkan promosi atau penawaran menarik yang ditargetkan khusus pada pelanggan dengan tingkat keanggotaan rendah dapat diimplementasikan. Selain itu, menyediakan promosi seperti penawaran untuk anggota baru juga bisa efektif.
3. Berdasarkan visualisasi di atas, dapat diamati bahwa nilai transaksi rata-rata untuk pelanggan yang kemungkinan akan churn cukup tinggi. Oleh karena itu, jika masalah ini tidak ditangani, perusahaan akan menghadapi dampak negatif yang signifikan, terutama dalam hal kerugian laba yang tinggi.
4. Banyak variabel yang tidak memiliki korelasi yang baik dengan variabel target. Variabel yang memiliki skor korelasi kuat dengan variabel target adalah 'membership_category', 'avg_transaction_value', 'avg_frequency_login_days', 'points_in_wallet', dan 'feedback'.

Kesimpulan Modelling:

Berdasarkan Analisis Model yang dilakukan, diputuskan bahwa model Sequential yang ditingkatkan adalah pendekatan pemodelan Jaringan Saraf Tiruan (ANN) terbaik untuk memprediksi risiko churn pelanggan. Berikut adalah temuan-temuan mengenai model yang digunakan:

Dengan skor evaluasi semua metrik sebesar 93%, model ini cukup baik untuk digunakan dalam prediksi kasus nyata.
Model ini mendapatkan skor recall tertinggi pada label 0 (pelanggan yang berisiko churn) dan mendapatkan skor false negative terendah sehingga membuat model ini lebih akurat dalam memprediksi "pelanggan yang tidak berisiko churn yang diprediksi sebagai pelanggan yang berisiko churn".

Business Insight:

Penawaran promosi atau penawaran menarik yang ditargetkan khusus pada pelanggan dengan tingkat keanggotaan rendah dapat diimplementasikan. Selain itu, menyediakan promosi seperti penawaran untuk anggota baru juga bisa efektif.
Dengan menargetkan segmen tertentu, bisnis dapat berusaha mempertahankan pelanggan yang sudah ada dengan tingkat keanggotaan rendah dan menarik pelanggan baru melalui penawaran yang menarik. Penting untuk menciptakan insentif yang personal dan menarik untuk mendorong loyalitas pelanggan dan meminimalkan churn.
Perusahaan dapat mempertimbangkan untuk menerapkan strategi retensi yang khusus menargetkan pelanggan bernilai tinggi. Strategi ini dapat mencakup penawaran personal, program loyalitas, atau peningkatan layanan pelanggan yang disesuaikan dengan kebutuhan mereka. Dengan memberikan insentif dan pengalaman pelanggan yang positif, perusahaan dapat mendorong pelanggan ini untuk tetap setia dan terus melakukan transaksi bernilai tinggi.
Untuk pemodelan yang telah dilakukan, proses pemodelan dapat ditingkatkan lebih lanjut, terutama dalam hal penyetelan hiperparameter. Mencari parameter yang lebih optimal yang dapat digunakan, berpotensi menghasilkan kinerja model yang lebih baik.

Penyetelan hiperparameter adalah langkah penting dalam mengoptimalkan kinerja model. Dengan secara sistematis mengubah hiperparameter dan mengevaluasi kinerja model pada data validasi.

Jika lebih banyak waktu diberikan untuk penyetelan hiperparameter, tidak ada yang tidak mungkin untuk mendapatkan model yang lebih akurat yang dapat memprediksi Churn Pelanggan dengan lebih baik.
