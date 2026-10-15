#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedilerin Gizli Felsefesi
=========================
Bu program, kedilerin mırıldanmalarını ve miyavlarını derin felsefi çıkarımlara çevirir.
Tamamen bilimsel bir çalışmadır. Şaka değil.
"""

import random
import time
import sys

FELSEFELER = [
    "Miyav... yani aslında varlık yokluk meselesi üzerine düşünüyordum. Kutu açılınca her şey değişir.",
    "İnsanlar neden bu kadar acele ediyor? Güneş ışığı yeterince felsefi değil mi?",
    "Kuyruk sallamak bir iletişim biçimidir. Ama kimse dinlemiyor. Bu trajik.",
    "Mama kasesi boşken evrenin anlamını sorgulamak gerekir. Doluysa sorgulamaya gerek yoktur.",
    "Uyumak, aslında en yüksek bilinç halidir. Descartes yanılıyordu.",
    "Pencere kenarında oturmak meditasyondur. Kuşlar sadece dikkat dağıtıcıdır.",
    "Kediler olarak biz, zamanın lineer olmadığını biliriz. Çünkü biz her zaman şimdideyiz.",
    "Tırmalamak bir sanat formudur. Mobilya sadece tuvaldir.",
]

MIYAVLAR = ["miyav", "mır mır", "meow", "mrrrr", "hıss", "purr"]

def felsefe_uret():
    print("\n🐱 Kedi düşünüyor...", end="", flush=True)
    for _ in range(3):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print("\n")
    felsefe = random.choice(FELSEFELER)
    miyav = random.choice(MIYAVLAR)
    print(f"[{miyav.upper()}] {felsefe}")
    print("\n--- Bu derin düşünce, bilimsel olarak doğrulanmıştır. ---")

def main():
    print("=" * 50)
    print("KEDİLERİN GİZLİ FELSEFESİ v1.0")
    print("Bilimsel Araştırma Aracı - Çok Ciddi")
    print("=" * 50)
    print("\nÇıkmak için 'q' yazın.\n")
    
    while True:
        girdi = input("Kediye miyav söyle (veya Enter'a bas): ").strip().lower()
        if girdi == 'q':
            print("\nKedi uyumaya gitti. Felsefe bitti. Hoşça kal.")
            break
        felsefe_uret()
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAni bir uyku moduna geçildi. Program sonlandı.")
        sys.exit(0)
