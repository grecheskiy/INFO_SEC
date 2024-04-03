import hashlib

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Чтение файла блоками для эффективности
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

file_path = "AI.docx"

actual_hash = calculate_hash(file_path)
print(actual_hash)

expected_hash = input('Enter String to hash: ')

if actual_hash == expected_hash:
    print("Целостность файла подтверждена.")
else:
    print("Файл был изменен или поврежден.")
