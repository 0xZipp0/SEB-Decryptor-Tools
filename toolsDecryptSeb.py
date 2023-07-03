import gzip
import zlib
import rncryptor

class RNCryptor_modified(rncryptor.RNCryptor):
    def post_decrypt_data(self, data):
        data = data[:-(data[-1])]
        return data

def decrypt_SEB():
    # Meminta pengguna memasukkan nama file encrypted.seb
    encrypted_seb_file = input("Masukkan nama file encrypted.seb: ")

    # Meminta pengguna memasukkan kata sandi
    password = input("Masukkan kata sandi: ")

    cryptor = RNCryptor_modified()

    with gzip.open(encrypted_seb_file, 'rb') as f:
        file_content = f.read()

    decrypted_data = cryptor.decrypt(file_content[4:], password)
    decompressed_data = zlib.decompress(decrypted_data, 15 + 32)

    # Meminta pengguna memasukkan nama file decrypted.seb
    decrypted_seb_file = input("Masukkan nama file decrypted.seb: ")

    with open(decrypted_seb_file, "wb") as f:
        f.write(decompressed_data)

decrypt_SEB()
