Satriya Fauzan Adhim

RMT 019

# Home Credit - Credit Default Risk Prediction

Project ini memiliki tujuan untuk melakukan analisa dan membuat pemodelan untuk melakukan prediksi pengklasifikasian resiko kredit default. Dataset yang digunakan merupakan dataset yang berisikan data-data mengenai debitor. Pengklasifikasian yang dibuat bertujuan untuk mengklasifikasi dan memprediksi apakah debitor akan melakukan pembayaran yang default atau tidak.

## Deployment Link
Deployment : https://huggingface.co/spaces/kodokgodog/Credit_Home

## Permasalahan

Permasalahan yang ada di dalam project ini adalah, diperlukannya pengembangan model klasifikasi untuk melakukan prediksi kemungkinan resiko kredit default yang akurat. Model ini dibuat dan akan dilatih yang selanjutnya dievaluasi dengan menggunaka beberapa algoritma machine learning, adapun algoritma yang digunakan adalah SVM, XGBoost dan LightGBM. Ketiga model tersebut akand dievaluasi menggunakan metrik ROC-AUC, akurasi, dan recall. Dengan tujuan untuk memperoleh model yang memiliki kinerja yang paling baik untuk digunakan di dalam pembuatan prediksi.

## Deskripsi Data

Dataset ini terdiri dari informasi klien, termasuk fitur demografi seperti usia, jenis kelamin, status perkawinan, dan tingkat pendidikan, serta fitur transaksi seperti jumlah pinjaman, riwayat pembayaran, dan penggunaan kredit. Variabel target adalah status risiko kredit default, yang menunjukkan apakah klien mengalami pembayaran default atau tidak.

## Evaluasi Model

Model akan dievaluasi berdasarkan kemampuannya dalam mengklasifikasikan risiko kredit default dengan benar. Metrik evaluasi utamanya adalah ROC-AUC, yang memberikan penilaian keseluruhan terhadap kemampuan model dalam membedakan kasus risiko default dan bukan default. Metrik tambahan seperti akurasi, presisi, dan recall akan digunakan untuk analisis lebih lanjut dan penilaian performa model.

## Alur Proyek

1. Preproses data: Lakukan pembersihan data, penanganan nilai yang hilang, penanganan outlier, dan pengkodean fitur kategori.
2. Rekayasa fitur: Buat fitur tambahan jika diperlukan dan pilih fitur yang relevan.
3. Pelatihan model: Latih beberapa model pembelajaran mesin termasuk SVM, XGBoost, dan LightGBM.
4. Evaluasi model: Evaluasi model menggunakan berbagai metrik seperti ROC-AUC, akurasi, presisi, dan recall.
5. Hyperparameter Tuning: Dilakukan untuk mengoptimalkan model yang dipilih dengan memilih hiperparameter menggunakan teknik seperti Random Search.
6. Pemilihan model akhir: Memilih model dengan performa terbaik berdasarkan metrik evaluasi.
7. Inferensi model

## Kesimpulan

XGB merupakan model yang telah dilatih dan dilakukan parameter tuning sehingga memberikan performa terbaik diantara 3 model yang telah dicoba. Berdasarkan pemodelan yang telah dilakukan maka diputuskan bahwa XGB merupakan pemodelan yang menunjukkan kinerja terbaik diantara 3 model yang diuji untuk memprediksi default payment dari debitur. Hasil evaluasi terakhir menunjukkan bahwa model XGB menghasilkan nilai ROC AUC Score sebesar 0.73 dan recall sebesar 0.68.

Dengan menggunakan pemodelan XGB yang telah dioptimalkan, PT Home Credit Indonesia dapat memprediksi dengan lebih akurat kemungkinan risiko kredit default pada klien mereka. Hal ini akan membantu perusahaan dalam mengambil keputusan yang tepat terkait pengelolaan pinjaman, penentuan suku bunga yang tepat, dan evaluasi kelayakan keuangan peminjam.

Penggunaan model prediksi risiko kredit default ini dapat membantu PT Home Credit Indonesia dalam mengurangi risiko keuangan, meningkatkan efisiensi pengelolaan dana pinjaman, dan memastikan stabilitas bisnis pembiayaan.
