import time
import random

def tampilkan_intro():
    print("\n" + "="*60)
    print("   SELAMAT DATANG DI DUNIA MISTERI PETUALANGAN")
    print("="*60)
    print()

def game_utama():
    tampilkan_intro()
    nama = input("Siapa namamu? ")
    print(f"\nSelamat datang, {nama}!")
    print("Kamu berada di persimpangan jalan yang sunyi...")
    time.sleep(1)
    
    print("\nDi depanmu ada dua jalan:")
    print("1. Jalur ke HUTAN MISTERIUS (penuh dengan monster)")
    print("2. Jalur ke KERAJAAN KERAJAAN (tempat kamu menjadi buronan)")
    
    while True:
        pilihan = input("\nPilih jalur mana (1 atau 2)? ")
        if pilihan == "1":
            jalur_hutan(nama)
            break
        elif pilihan == "2":
            jalur_kerajaan(nama)
            break
        else:
            print("Masukan tidak valid! Pilih 1 atau 2.")

def jalur_hutan(nama):
    print(f"\n{'='*60}")
    print("JALUR HUTAN MISTERIUS")
    print(f"{'='*60}")
    print(f"\n{nama} memasuki hutan yang gelap dan suram...")
    time.sleep(1)
    
    # Player stats
    health = 200
    max_health = 200
    weapon = None
    weapon_power = 0
    monster_count = 0
    
    # Tahap 1: Bertemu monster tanpa senjata
    print("\nKamu berjalan beberapa langkah...")
    print("Tiba-tiba, seekor GOBLIN LIAR menyerangmu!")
    time.sleep(1)
    
    while monster_count < 2:
        # Monster tier berbeda di setiap encounter
        monster_tier = monster_count + 1  # Tier 1 dan 2
        monster_name = ["GOBLIN LIAR", "ORC RAKUS"][monster_count]
        monster_tier_text = ["TIER 1 (Lemah)", "TIER 2 (Menengah)"][monster_count]
        
        print(f"\n[Health: {health}/{max_health}]")
        print(f"Sebuah {monster_name} [{monster_tier_text}] menghadang jalan!")
        print("Apa yang kamu lakukan?")
        print("1. Mencoba melawan dengan tangan kosong")
        print("2. Berlari meninggalkan monster")
        
        pilihan = input("\nPilih (1 atau 2): ")
        if pilihan == "1":
            damage_dealt = random.randint(5, 15)
            # Damage monster tergantung tier: Tier 1 = 10-20, Tier 2 = 20-35
            damage_taken = random.randint(10 + (monster_tier * 5), 20 + (monster_tier * 7))
            print(f"\nKamu mencoba melawan dengan tangan kosong...")
            print(f"Kamu memberikan damage: {damage_dealt}")
            print(f"{monster_name} memberikan damage pada dirimu: {damage_taken}")
            health -= damage_taken
            
            if health <= 0:
                print(f"\nKamu terlalu lemah... Kamu mati dimakan monster!")
                print(f"GAME OVER - Tidak ada senjata untuk melawan!")
                return
            
            monster_count += 1
            print(f"Monster berhasil kamu usir! Melanjutkan perjalanan...")
            time.sleep(1)
        elif pilihan == "2":
            print("Kamu berlari secepat mungkin...")
            monster_count += 1
            time.sleep(1)
        else:
            print("Pilihan tidak valid!")
    
    # Tahap 2: Menemukan toko pedang
    print(f"\n{'='*40}")
    print("TOKO ALAT PEDANG")
    print(f"{'='*40}")
    print(f"\n{nama} menemukan sebuah toko tua di tengah hutan!")
    print("Pemilik toko: 'Selamat datang, traveler! Pilih pedangmu!'")
    time.sleep(1)
    
    print("\nPilihan Pedang:")
    print("1. PEDANG KAYU (Kekuatan: 10, hanya buat pemula)")
    print("2. PEDANG BESI (Kekuatan: 25, standar yang baik)")
    print("3. PEDANG LEGENDARIS (Kekuatan: 40, sangat kuat tapi jarang)")
    
    while True:
        pilihan_pedang = input("\nPilih pedang (1, 2, atau 3): ")
        if pilihan_pedang == "1":
            weapon = "Pedang Kayu"
            weapon_power = 10
            print(f"Kamu mengambil {weapon}! (Kekuatan: {weapon_power})")
            break
        elif pilihan_pedang == "2":
            weapon = "Pedang Besi"
            weapon_power = 25
            print(f"Kamu mengambil {weapon}! (Kekuatan: {weapon_power})")
            break
        elif pilihan_pedang == "3":
            weapon = "Pedang Legendaris"
            weapon_power = 40
            print(f"Kamu mengambil {weapon}! (Kekuatan: {weapon_power})")
            print("Pemilik toko melirikmu dengan kagum!")
            break
        else:
            print("Pilihan tidak valid!")
    
    time.sleep(1)
    
    # Tahap 3: Pertarungan menjelang boss
    print(f"\n{'='*40}")
    print("AREA PERTARUNGAN AKHIR")
    print(f"{'='*40}")
    print(f"\n{nama} melanjutkan perjalanan dengan {weapon}...")
    print("Area ini terasa sangat berbeda... Udara menjadi dingin!")
    print("Tiba-tiba... BOSS MONSTER MUNCUL!!!")
    time.sleep(2)
    
    print("\n" + "!"*40)
    print("  RAJA MONSTER HUTAN MUNCUL!")
    print("  Kekuatan luar biasa, mata yang menyala merah!")
    print("!"*40)
    
    boss_health = 150  # Boss lebih tangguh
    player_health = health
    boss_tier = 4  # Boss adalah tier 4
    
    # Battle dengan boss
    round_num = 1
    while boss_health > 0 and player_health > 0:
        print(f"\n[ROUND {round_num}]")
        print(f"RAJA MONSTER [TIER 4 - ELITE] Health: {boss_health}/{150}")
        print(f"{nama} Health: {player_health}/{max_health}")
        print("\nApa strateguimu?")
        print("1. Serang dengan pedang secara langsung")
        print("2. Menghindar dan mencari kelemahan")
        
        pilihan_boss = input("\nPilih (1 atau 2): ")
        
        if pilihan_boss == "1":
            damage = weapon_power + random.randint(5, 15)
            # Boss Tier 4: damage 40-60
            boss_damage = random.randint(40, 60)
            
            print(f"\nKamu menyerang dengan ganas!")
            print(f"Damage yang diberikan: {damage}")
            boss_health -= damage
            
            if boss_health > 0:
                print(f"Boss membalas seranganmu dengan keras dan brutal!")
                print(f"Damage yang diterima: {boss_damage} (TIER 4 - SANGAT KUAT!)")
                player_health -= boss_damage
        
        elif pilihan_boss == "2":
            print(f"\nKamu menghindar dan mencari celah!")
            dodge = random.randint(1, 2)
            
            if dodge == 1:
                damage = weapon_power + random.randint(15, 25)
                print(f"Kamu menemukan kelemahan! Seranganmu sangat efektif!")
                print(f"Damage yang diberikan: {damage}")
                boss_health -= damage
            else:
                boss_damage = random.randint(45, 65)
                print(f"Boss masih berhasil mencuri serangan dengan ganas!")
                print(f"Damage yang diterima: {boss_damage} (TIER 4 - SERANGAN BERBAHAYA!)")
                player_health -= boss_damage
        else:
            print("Pilihan tidak valid!")
            continue
        
        round_num += 1
        time.sleep(1)
    
    # Hasil akhir jalur hutan
    if player_health > 0:
        print(f"\n{'='*60}")
        print("KEMENANGAN!!")
        print(f"{'='*60}")
        print(f"\n{nama} berhasil mengalahkan RAJA MONSTER HUTAN!")
        print(f"Hutan kini aman dari teror monster...")
        print(f"\nHEALTH AKHIR: {player_health}")
        print(f"\n🎉 SELAMAT! GAME SELESAI! 🎉")
        print(f"Kamu adalah HERO HUTAN!")
    else:
        print(f"\n{'='*60}")
        print("KEKALAHAN!")
        print(f"{'='*60}")
        print(f"\n{nama} jatuh di tempat... Boss mengaum kemenangan!")
        print(f"\nGAME OVER - Kamu tidak cukup kuat!")

def jalur_kerajaan(nama):
    print(f"\n{'='*60}")
    print("JALUR KERAJAAN BERBAHAYA")
    print(f"{'='*60}")
    print(f"\n{nama} secara tidak sengaja memasuki Kerajaan Terlarang...")
    print("Seorang penjaga melihat wajahmu: 'PENGGANGGU! TANGKAP DIA!'")
    print("Kamu adalah BURONAN KERAJAAN!")
    time.sleep(2)
    
    # Player stats
    health = 200
    max_health = 200
    spotted = 0
    disguise_active = False
    escape_progress = 0
    
    # Area 1: Jalan Utama Kerajaan
    print(f"\n{'='*40}")
    print("AREA 1: JALAN UTAMA KERAJAAN")
    print(f"{'='*40}")
    print("\nKamu berlari memasuki kerajaan yang ramai...")
    print("Tentara berbondong-bondong mengejar! Kamu harus cepat!")
    time.sleep(1)
    
    while escape_progress < 1:
        print(f"\n[Health: {health}/{max_health}]")
        print(f"Kamu melihat dua pilihan:")
        print("1. Bersembunyi di kerumunan pasar (area ramai)")
        print("2. Merampok pakaian penjual dan menyamar")
        
        pilihan = input("\nPilih (1 atau 2): ")
        
        if pilihan == "1":
            detected = random.randint(1, 2)
            if detected == 1:
                spotted += 1
                # Penjaga Tier 1: damage 15-25
                damage = random.randint(15, 25)
                print("Kamu bersembunyi di kerumunan, tapi penjaga melihat kamu!")
                print(f"Penjaga [TIER 1] menyerangmu dengan pedang!")
                print(f"Damage diterima: {damage}")
                health -= damage
                if health <= 0:
                    print(f"\nKamu terluka parah dan tertangkap!")
                    print(f"GAME OVER - Kesehatan tidak cukup!")
                    return
                print(f"Tingkat kesadaran: {spotted}/3")
            else:
                print("Kamu berhasil menyamar di antara kerumunan pasar!")
                escape_progress += 1
        
        elif pilihan == "2":
            print("Kamu merampok pakaian penjual dan berpakaian seperti warga biasa!")
            disguise_active = True
            print("Kamu sekarang TERSEMBUNYI dengan baik!")
            escape_progress += 1
        else:
            print("Pilihan tidak valid!")
    
    # Area 2: Istana Kerajaan
    print(f"\n{'='*40}")
    print("AREA 2: LORONG ISTANA KERAJAAN")
    print(f"{'='*40}")
    print("\nKamu memasuki lorong istana yang megah...")
    escape_progress = 0
    tentara_area = 0
    
    while escape_progress < 1:
        print(f"\n[Health: {health}/{max_health}]")
        print(f"Kamu melihat penjaga di setiap sudut lorong!")
        print("1. Memanfaatkan penyamaran, berjalan santai seperti pelayan")
        print("2. Mencuri senjata dan menciptakan kebingungan")
        
        pilihan = input("\nPilih (1 atau 2): ")
        
        if pilihan == "1":
            if disguise_active:
                print("Penyamaranmu berhasil! Penjaga tidak mencurigaimu!")
                print("Kamu berjalan santai melewati penjaga...")
                escape_progress += 1
            else:
                spotted += 1
                # Penjaga Tier 2: damage 25-40
                damage = random.randint(25, 40)
                print("Tanpa penyamaran, penjaga mengenali dirimu!")
                print(f"Penjaga [TIER 2] menyerangmu dengan sengit!")
                print(f"Damage diterima: {damage}")
                health -= damage
                if health <= 0:
                    print(f"\nKamu terluka parah dan tertangkap!")
                    print(f"GAME OVER - Kesehatan tidak cukup!")
                    return
                print(f"Tingkat kesadaran: {spotted}/3")
        
        elif pilihan == "2":
            print("Kamu mencuri senjata dari jejeran senjata di dinding!")
            print("ALARM BERBUNYI! SELURUH KERAJAAN DALAM SIAGA MAKSIMAL!")
            spotted += 1
            # Penjaga Tier 3 muncul: damage 35-50
            damage = random.randint(35, 50)
            print(f"Penjaga [TIER 3 - ELITE] datang merespons alarm!")
            print(f"Damage diterima: {damage}")
            health -= damage
            if health <= 0:
                print(f"\nKamu terluka parah dan tertangkap!")
                print(f"GAME OVER - Kesehatan tidak cukup!")
                return
            print(f"Tingkat kesadaran: {spotted}/3")
        else:
            print("Pilihan tidak valid!")
        
        if spotted >= 3:
            print("\nTENTARA BERHASIL MENGEJAR POSISIMU!")
            print(f"Banyak penjaga [TIER 2-3] mengepung dirimu!")
            print(f"GAME OVER - Kesehatan dan kesadaran habis!")
            return
    
    # Area 3: Gerbang Kerajaan Terakhir
    print(f"\n{'='*60}")
    print("AREA 3: GERBANG KERAJAAN - PERTAHANAN TERAKHIR")
    print(f"{'='*60}")
    print(f"\n[Health: {health}/{max_health}]")
    print("\nKamu sampai di gerbang keluar kerajaan...")
    print("Tapi... RATUSAN TENTARA BERDIRI DI DEPAN GERBANG!")
    print("Komandan Tentara [TIER 4 - LEGENDARY] berdiri di garis depan!")
    print("Sang Raja sendiri mengobservasi situasimu dari tahta!")
    time.sleep(2)
    
    print("\nKamu adalah korban yang gagal lolos...")
    print("TAPI TUNGGU! Ada tiga cara untuk lolos dari sini:")
    print("\n1. CARA KASAR: Bertarung melawan ratusan tentara")
    print("2. CARA LICIK: Gunakan kecerdikan untuk mengalihkan perhatian mereka")
    print("3. CARA TULUS: Menyerah dan memohon belas kasihan Raja")
    
    final_choice = input("\nPilih caramu lolos (1, 2, atau 3): ")
    
    if final_choice == "1":
        print("\n" + "!"*50)
        print("KAMU MEMUTUSKAN UNTUK BERTARUNG!")
        print("!"*50)
        print("\nKamu berlari menyerang dengan berani!")
        print("Ratusan tentara [Tier 1-4] menyerangmu dari segala arah...")
        print("Pertempuran sengit terjadi... Nyawa gantung di benang halus...")
        time.sleep(2)
        
        # Battle phase - mengalami damage dari multiple tiers
        enemy_waves = [
            {"name": "Tentara Biasa [TIER 1]", "damage_range": (15, 25), "count": 30},
            {"name": "Tentara Terlatih [TIER 2]", "damage_range": (25, 40), "count": 20},
            {"name": "Pemenang Medali [TIER 3]", "damage_range": (35, 50), "count": 10},
            {"name": "Komandan Tentara [TIER 4]", "damage_range": (45, 70), "count": 1}
        ]
        
        total_damage = 0
        for wave in enemy_waves:
            damage = random.randint(wave["damage_range"][0], wave["damage_range"][1])
            total_damage += damage
            print(f"\n{wave['name']} ({wave['count']} orang) menyerangmu!")
            print(f"Damage yang diterima: {damage}")
        
        health -= total_damage
        print(f"\nTotal damage yang diterima: {total_damage}")
        print(f"Sisa health: {health}/{max_health}")
        
        if health > 0:
            print("\nDENG! DEEEENG! DEEEENG! BUNYI PEDANG BERTABRAKAN!")
            print("Dengan kekuatan penuh dan keberuntungan, kamu berhasil terobos!")
            print("Kamu berlari keluar dari kerajaan dengan selamat!")
            print(f"\n🏃 {nama} BERHASIL LOLOS DARI KERAJAAN! 🏃")
            print("Kamu kini adalah LEGENDA PELARI KERAJAAN!")
        else:
            print("\nTentara terlalu banyak dan kuat... Kamu tertangkap!")
            print("GAME OVER - Kesehatan tidak cukup untuk melawan semua!")
    
    elif final_choice == "2":
        print("\n" + "💡"*25)
        print("KAMU MENGGUNAKAN KECERDIKAN!")
        print("💡"*25)
        print("\nKamu melempar obor ke gudang senjata!")
        print("LEDAKAN BESAR! GUDANG SENJATA MELEDAK!")
        print("Semua tentara berlarian menuju sumber ledakan!")
        print("Kesempatan! Kamu berlari keluar dari kerajaan!")
        time.sleep(2)
        print(f"\n✨ {nama} BERHASIL LOLOS DENGAN CERDIK! ✨")
        print("Kamu kini adalah MAESTRO STRATEGI!")
    
    elif final_choice == "3":
        print("\n" + "🤝"*25)
        print("KAMU MEMILIH JALAN TULUS!")
        print("🤝"*25)
        print("\nKamu berlutut dan memohon kepada Raja...")
        print("Raja terkejut dengan keberanian dan kejujuranmu!")
        print("Raja tersenyum: 'Kamu punya hati yang tulus...'")
        print("'Saya memberikanmu kesempatan... PERGI DARI KERAJAAN INI!'")
        print("Tentara membuka jalan untuk dirimu...")
        time.sleep(2)
        print(f"\n❤️  {nama} LOLOS BERKAT BELAS KASIHAN RAJA! ❤️")
        print("Kamu kini adalah 'YANG BERBELAS KASIHAN'!")
    else:
        print("Pilihan tidak valid! Kamu tertangkap!")
    
    print(f"\n{'='*60}")
    print("SELAMAT! GAME SELESAI!")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    game_utama()