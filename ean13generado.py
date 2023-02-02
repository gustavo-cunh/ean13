def calc_ean13_check_digit(ean13_code):
    check_sum = 0
    for i in range(12):
        if i % 2 == 0:
            check_sum += int(ean13_code[i])
        else:
            check_sum += int(ean13_code[i]) * 3
    check_digit = (10 - (check_sum % 10)) % 10
    return str(check_digit)

def calc_ean13_check_digit(ean13_code):
    check_sum = 0
    for i in range(12):
        if i % 2 == 0:
            check_sum += int(ean13_code[i])
        else:
            check_sum += int(ean13_code[i]) * 3
    check_digit = (10 - (check_sum % 10)) % 10
    return str(check_digit)

def generate_ean13_codes(num_codes, cnpj_first_five):
    ean13_codes = []
    for i in range(num_codes):
        sequential_number = str(i).zfill(4)
        ean13_code = "789" + cnpj_first_five + sequential_number
        check_digit = calc_ean13_check_digit(ean13_code)
        full_ean13_code = ean13_code + check_digit
        ean13_codes.append(full_ean13_code)
    return ean13_codes

num_codes = int(input("Quantos códigos EAN13 você deseja gerar? "))
cnpj_first_five = input("Insira os 5 primeiros dígitos do CNPJ: ")

ean13_codes = generate_ean13_codes(num_codes, cnpj_first_five)
for code in ean13_codes:
    print("Código EAN13 gerado: {}".format(code))

