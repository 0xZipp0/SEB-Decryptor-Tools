# SEB-Decryptor-Tools By YTCraft

Berikut adalah penjelasan fungsi dan kegunaan dari setiap bagian kode dalam bahasa Python yang Anda berikan:

1. import gzip: Ini adalah pernyataan impor yang digunakan untuk mengimpor modul gzip. Modul ini digunakan untuk kompresi dan dekompresi file dengan format gzip.
2. import zlib: Ini adalah pernyataan impor yang digunakan untuk mengimpor modul zlib. Modul ini digunakan untuk kompresi dan dekompresi data menggunakan algoritma zlib.
3. import rncryptor: Ini adalah pernyataan impor yang digunakan untuk mengimpor modul rncryptor. Modul ini berisi implementasi enkripsi dan dekripsi menggunakan algoritma RNCryptor.
4. class RNCryptor_modified(rncryptor.RNCryptor):: Ini adalah definisi kelas RNCryptor_modified yang merupakan turunan dari kelas rncryptor.RNCryptor. Kelas ini diturunkan untuk memodifikasi perilaku setelah dekripsi data.
5. def post_decrypt_data(self, data):: Ini adalah metode kelas yang disebut post_decrypt_data. Metode ini mengambil data hasil dekripsi sebagai argumen dan memodifikasinya dengan menghapus padding yang ditambahkan selama enkripsi. Metode ini mengembalikan data yang telah dimodifikasi.
6. def decrypt_SEB():: Ini adalah definisi fungsi decrypt_SEB yang tidak menerima argumen. Fungsi ini akan meminta pengguna untuk memasukkan nama file "encrypted.seb" dan kata sandi. Kemudian, fungsi ini akan melakukan dekripsi dan dekompresi file "encrypted.seb" menggunakan kata sandi yang diberikan. Hasil dekompresi akan disimpan dalam file yang ditentukan oleh pengguna dengan nama "decrypted.seb".
7. encrypted_seb_file = input("Masukkan nama file encrypted.seb: "): Ini adalah pernyataan yang meminta pengguna untuk memasukkan nama file "encrypted.seb" melalui terminal dan menyimpannya dalam variabel encrypted_seb_file.
8. password = input("Masukkan kata sandi: "): Ini adalah pernyataan yang meminta pengguna untuk memasukkan kata sandi melalui terminal dan menyimpannya dalam variabel password.
9. cryptor = RNCryptor_modified(): Ini adalah pernyataan yang membuat objek RNCryptor_modified. Objek ini akan digunakan untuk melakukan dekripsi dengan memanggil metode decrypt dari modul RNCryptor.
10. with gzip.open(encrypted_seb_file, 'rb') as f: ...: Ini adalah blok kode yang membuka file "encrypted.seb" menggunakan modul gzip dan membaca isinya. Isi file kemudian disimpan dalam variabel file_content.
11. decrypted_data = cryptor.decrypt(file_content[4:], password): Ini adalah pernyataan yang memanggil metode decrypt dari objek cryptor untuk melakukan dekripsi data yang dibaca dari file "encrypted.seb". Metode ini membutuhkan argumen berupa data yang akan didekripsi dan kata sandi yang digunakan.
12. decompressed_data = zlib.decompress(decrypted_data, 15 + 32): Ini adalah pernyata
