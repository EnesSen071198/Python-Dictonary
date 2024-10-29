# Sözlük (Dictionary) Örneği / Dictionary Example
fitness_dictionary = {"banana": 100, "apple": 200, "melon": 300}  # Farklı yiyeceklerin kalorilerini içeren bir sözlük / Dictionary with calorie values of different foods

# Sözlüğün değerlerini yazdırma / Print dictionary values
print("Değerler (values): ", fitness_dictionary.values())  # Sözlükteki tüm değerleri gösterir / Shows all values in the dictionary

# Sözlüğün anahtarlarını yazdırma / Print dictionary keys
print("Anahtarlar (keys): ", fitness_dictionary.keys())  # Sözlükteki tüm anahtarları gösterir / Shows all keys in the dictionary

# Sözlükteki tüm elemanları yazdırma / Print all items in dictionary
print("Elemanlar (items): ", fitness_dictionary.items())  # Sözlükteki tüm anahtar-değer çiftlerini gösterir / Shows all key-value pairs in the dictionary

# Belli anahtarların değerlerine erişim / Accessing values of specific keys
print("Muz kalorisi (banana calories): ", fitness_dictionary["banana"])  # Sözlükten muz kalorisi / Get banana's calorie from the dictionary
print("Elma kalorisi (apple calories): ", fitness_dictionary["apple"])  # Sözlükten elma kalorisi / Get apple's calorie from the dictionary
print("Kavun kalorisi (melon calories): ", fitness_dictionary["melon"])  # Sözlükten kavun kalorisi / Get melon's calorie from the dictionary

# Sözlükteki değeri güncelleme / Update value in dictionary
fitness_dictionary["banana"] = 500  # Muzun kalorisi güncellenir / Update banana's calorie
print("Güncellenmiş muz kalorisi (Updated banana calories): ", fitness_dictionary["banana"])

# Sözlüğe yeni eleman ekleme / Add new item to dictionary
fitness_dictionary["orange"] = 150  # Yeni bir anahtar-değer çifti ekler / Adds a new key-value pair
print("Yeni sözlük (New dictionary): ", fitness_dictionary)

# Bir elemanı sözlükten silme / Remove an item from dictionary
del fitness_dictionary["apple"]  # Elma anahtarını ve değerini sözlükten kaldırır / Removes apple key and value from the dictionary
print("Elmadan sonra sözlük (Dictionary after removing apple): ", fitness_dictionary)

# Sözlükte bir anahtarın olup olmadığını kontrol etme / Check if key exists in dictionary
print("Sözlükte muz var mı? (Is 'banana' in dictionary?): ", "banana" in fitness_dictionary)  # 'banana' anahtarının olup olmadığını kontrol eder / Checks if 'banana' key is in dictionary
print("Sözlükte elma var mı? (Is 'apple' in dictionary?): ", "apple" in fitness_dictionary)

# Sözlükteki tüm elemanları temizleme / Clear all items in dictionary
fitness_dictionary.clear()  # Tüm elemanları sözlükten siler / Removes all elements from the dictionary
print("Temizlenmiş sözlük (Cleared dictionary): ", fitness_dictionary)
