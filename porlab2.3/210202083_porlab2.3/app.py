from flask import Flask, request, jsonify, render_template, send_file
from sqlalchemy.exc import IntegrityError
import mysql.connector

app = Flask(__name__)

# MySQL bağlantısı
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fb123456",
    database="hastane_db"
)

# Ana sayfa
@app.route('/')
def ana_sayfa():
    return render_template('index.html')

# Tüm hastaları getirme
@app.route('/tum_hastalar', methods=['GET'])
def tum_hastalar():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM Hastalar")
    hastalar = mycursor.fetchall()
    return jsonify({"hastalar": hastalar})

# Tüm doktorları getirme
@app.route('/tum_doktorlar', methods=['GET'])
def tum_doktorlar():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM Doktorlar")
    doktorlar = mycursor.fetchall()
    return jsonify({"doktorlar": doktorlar})

# Tüm randevuları getirme
@app.route('/tum_randevular', methods=['GET'])
def tum_randevular():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM Randevular")
    randevular = mycursor.fetchall()
    return jsonify({"randevular": randevular})

# Hastanın tıbbi raporlarını getirme
@app.route('/hasta_raporlari/<int:hasta_id>', methods=['GET'])
def hasta_raporlari(hasta_id):
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM TibbiRaporlar WHERE HastaID = %s"
    mycursor.execute(sql, (hasta_id,))
    raporlar = mycursor.fetchall()
    return jsonify({"raporlar": raporlar})

# Hasta ekleme
@app.route('/hasta_ekle', methods=['POST'])
def hasta_ekle():
    try:
        data = request.json
        mycursor = mydb.cursor()
        sql = "INSERT INTO Hastalar (Ad, Soyad, DogumTarihi, Cinsiyet, TelefonNumarasi, Adres) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (data['ad'], data['soyad'], data['dogum_tarihi'], data['cinsiyet'], data['telefon'], data['adres'])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"message": "Hasta başarıyla eklendi."}), 201
    except KeyError:
        return jsonify({"error": "Eksik veya hatalı veri gönderildi."}), 400
    except IntegrityError:
        mydb.rollback()
        return jsonify({"error": "Hasta eklenirken bir hata oluştu."}), 400

# Hasta silme
@app.route('/hasta_sil/<int:hasta_id>', methods=['DELETE'])
def hasta_sil(hasta_id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM Hastalar WHERE HastaID = %s"
    val = (hasta_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    if mycursor.rowcount == 0:
        return jsonify({"error": "Hasta bulunamadı."}), 404
    return jsonify({"message": "Hasta başarıyla silindi."})

# Doktor ekleme
@app.route('/doktor_ekle', methods=['POST'])
def doktor_ekle():
    try:
        data = request.json
        mycursor = mydb.cursor()
        sql = "INSERT INTO Doktorlar (Ad, Soyad, UzmanlikAlani, CalistigiHastane) VALUES (%s, %s, %s, %s)"
        val = (data['ad'], data['soyad'], data['uzmanlik_alani'], data['calistigi_hastane'])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"message": "Doktor başarıyla eklendi."}), 201
    except KeyError:
        return jsonify({"error": "Eksik veya hatalı veri gönderildi."}), 400
    except IntegrityError:
        mydb.rollback()
        return jsonify({"error": "Doktor eklenirken bir hata oluştu."}), 400

# Doktor silme
@app.route('/doktor_sil/<int:doktor_id>', methods=['DELETE'])
def doktor_sil(doktor_id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM Doktorlar WHERE DoktorID = %s"
    val = (doktor_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    if mycursor.rowcount == 0:
        return jsonify({"error": "Doktor bulunamadı."}), 404
    return jsonify({"message": "Doktor başarıyla silindi."})

# Randevu ekleme
@app.route('/randevu_ekle', methods=['POST'])
def randevu_ekle():
    try:
        data = request.json
        mycursor = mydb.cursor()
        sql = "INSERT INTO Randevular (HastaID, DoktorID, RandevuTarihi) VALUES (%s, %s, %s)"
        val = (data['hasta_id'], data['doktor_id'], data['randevu_tarihi'])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"message": "Randevu başarıyla oluşturuldu."}), 201
    except KeyError:
        return jsonify({"error": "Eksik veya hatalı veri gönderildi."}), 400
    except IntegrityError:
        mydb.rollback()
        return jsonify({"error": "Randevu oluşturulurken bir hata oluştu."}), 400

# Randevu silme
@app.route('/randevu_sil/<int:randevu_id>', methods=['DELETE'])
def randevu_sil(randevu_id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM Randevular WHERE RandevuID = %s"
    val = (randevu_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    if mycursor.rowcount == 0:
        return jsonify({"error": "Randevu bulunamadı."}), 404
    return jsonify({"message": "Randevu başarıyla iptal edildi."})

# Tıbbi rapor ekleme
@app.route('/tibbi_rapor_ekle', methods=['POST'])
def tibbi_rapor_ekle():
    try:
        data = request.json
        mycursor = mydb.cursor()
        sql = "INSERT INTO TibbiRaporlar (HastaID, RaporIcerigi, RaporTarihi, RaporSonucu) VALUES (%s, %s, %s, %s)"
        val = (data['hasta_id'], data['rapor_icerigi'], data['rapor_tarihi'], data['rapor_sonucu'])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"message": "Tıbbi rapor başarıyla oluşturuldu."}), 201
    except KeyError:
        return jsonify({"error": "Eksik veya hatalı veri gönderildi."}), 400
    except IntegrityError:
        mydb.rollback()
        return jsonify({"error": "Tıbbi rapor oluşturulurken bir hata oluştu."}), 400

# Tıbbi rapor silme
@app.route('/tibbi_rapor_sil/<int:rapor_id>', methods=['DELETE'])
def tibbi_rapor_sil(rapor_id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM TibbiRaporlar WHERE RaporID = %s"
    val = (rapor_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    if mycursor.rowcount == 0:
        return jsonify({"error": "Tıbbi rapor bulunamadı."}), 404
    return jsonify({"message": "Tıbbi rapor başarıyla silindi."})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
