# -*- coding: utf-8 -*-
"""Kalkulator volume tabung.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cy3rTGU2XqM6lLCAIlWllLYDsFTMyvoP
"""

class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi ** 3


def main():
    try:
        sisi = float(input("Masukkan panjang sisi kubus (cm): "))
        if sisi <= 0:
            raise ValueError("Sisi harus lebih dari 0.")

        kubus = Kubus(sisi)
        print(f"Volume kubus adalah: {kubus.volume()} cm³")
    except ValueError as e:
        print(f"Input tidak valid: {e}")


if __name__ == "__main__":
    main()