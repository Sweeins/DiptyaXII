from flask import Flask, render_template, request, redirect
import random

Kuis = [
    {
        'Soal': "Apa nama",
        'Jawaban': ["Joni", "Rudi", "Tayo"],
        'Benar': "Joni"
    },
    {
        'Soal': "Apa nama",
        'Jawaban': ["Joni", "Rudi", "Tayo"],
        'Benar': "Joni"
    },
    {
        'Soal': "Apa nama",
        'Jawaban': ["Joni", "Rudi", "Tayo"],
        'Benar': "Joni"
    },
    {
        'Soal': "Apa nama",
        'Jawaban': ["Joni", "Rudi", "Tayo"],
        'Benar': "Joni"
    },
    {
        'Soal': "Apa nama",
        'Jawaban': ["Joni", "Rudi", "Tayo"],
        'Benar': "Joni"
    }
]

app = Flask(__name__)

def PilihSoal(Randoms):
    _Random = random.randint(0, len(Kuis))
    for Random in Randoms:
        if _Random == Random:
            _Random = PilihSoal(Randoms)
    return _Random

@app.route("/")
def Root():
    return render_template('Main.html')

Skor = []
SkorJikaBenar = 20
JumlahSoal = 2
StepSoal = []

@app.route("/mulai")
def Mulai():
    Randoms = []
    Skor.clear()
    Skor.append(0)
    StepSoal.append(0)
    for X in range(JumlahSoal):
        Randoms.append(PilihSoal(Randoms))
    return redirect("/soal")

@app.route("/soal", methods=["GET", "POST"])
def Soal():
    if request.method == "GET":
        return render_template("Soal.html", Kuis = Kuis[StepSoal[0]])
    else:
        JawabanDipilih = request.form.getlist("checkbox")[0]
        if JawabanDipilih == Kuis[StepSoal[0]]['Benar']:
            _Skor = Skor[0]
            Skor.clear()
            Skor.append(_Skor + 20)
        if StepSoal[0] == JumlahSoal - 1:
            return redirect("/hasil")
        _StepSoal = StepSoal[0]
        StepSoal.clear()
        StepSoal.append(_StepSoal + 1)
        return redirect("/soal")
        
@app.route("/hasil")
def Hasil():
    return render_template("Hasil.html", Skor=Skor[0])

app.run(port = 5000)