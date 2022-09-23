#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	taux_taxes = 0.15

	sous_total = sum([price[INDEX_PRICE]*price[INDEX_QUANTITY] for price in data])
	taxes = sous_total*taux_taxes
	total = sous_total + taxes
	titres = ("SOUS TOTAL", "TAXES", "TOTAL")

	output = "{} \n{:<10} {:>10.2f} $ \n{:<10} {:>10.2f} $ \n{:<10} {:>10.2f} $"\
		.format(name, titres[0], sous_total, titres[1], taxes, titres[2], total)

	return output


def format_number(number, num_decimal_digits):
	output = ""
	chiffre = number
	nbr_mul_10 = 0
	triplet = 0
	if chiffre < 0:
		chiffre *= -1

	while chiffre % 1 != 0:
		chiffre *= 10
		nbr_mul_10 += 1

	nbr_dec_skip = nbr_mul_10
	chiffre = int(chiffre)

	while chiffre != 0:
		caractere = str(chiffre % 10)
		chiffre //= 10
		if num_decimal_digits < nbr_dec_skip:
			nbr_dec_skip -= 1
			continue

		if nbr_dec_skip > 0:
			nbr_dec_skip -= 1
		else:
			if triplet != 3:
				triplet += 1
			else:
				output = " " + output
				triplet = 1

		output = caractere + output

	if nbr_mul_10 != 0:
		output = output[:-num_decimal_digits] + "." + output[-num_decimal_digits:]

	if number < 0:
		output = "-" + output

	return output

def get_triangle(num_rows):
	nbr_max_A_par_ligne = num_rows*2-1
	ligne_plus = "+"*(nbr_max_A_par_ligne+2) + "\n"
	output = ligne_plus
	A = "A"
	espace = " "

	for ligne in range(1, num_rows+1):
		lettre_par_ligne = ligne * 2 - 1
		espace_par_cote = int((nbr_max_A_par_ligne-lettre_par_ligne)/2)
		output += f"+{espace_par_cote*espace}{lettre_par_ligne*A}{espace_par_cote*espace}+\n"

	output += ligne_plus

	return output


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
