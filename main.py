import re

# Roma rakamlarının karşılık geldiği değerler
roman_numeral_map = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

# Geçerli Roma rakamı desenini tanımlıyoruz
valid_roman_pattern = re.compile(r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")

# Roma rakamını tam sayı (integer) değerine çeviren fonksiyon
def roman_to_integer(roman):
    if not valid_roman_pattern.match(roman):
        raise ValueError("Geçersiz Roma rakamı girdisi!")

    result = 0
    i = 0

    while i < len(roman):
        # Eğer iki harfli bir kombinasyon varsa, önce ona bakıyoruz
        if i + 1 < len(roman) and roman[i:i+2] in roman_numeral_map:
            result += roman_numeral_map[roman[i:i+2]]
            i += 2
        else:
            result += roman_numeral_map[roman[i]]
            i += 1

    return result

# Kullanıcıdan giriş alıp işleyen CLI fonksiyonu
def main():
    while True:
        roman_input = input("Bir Roma rakamı girin (çıkış için 'q' yazın): ").upper()
        if roman_input == 'Q':
            break
        try:
            integer_value = roman_to_integer(roman_input)
            if 1 <= integer_value <= 4999:
                print(f"Roma rakamı {roman_input}, Arap rakamı olarak: {integer_value}")
            else:
                print("Lütfen 1 ile 4999 arasında bir Roma rakamı girin.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
