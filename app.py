from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():

    # Membaca data CSV
    df = pd.read_csv("latihan1.csv")

    # Kolom numerik yang akan dianalisis
    kolom_analisis = [
        "Age",
        "Study_Hours",
        "Sleep_Hours",
        "Attendance",
        "Exam_Score",
        "Monthly_Spending",
        "Screen_Hours",
        "Satisfaction"
    ]

    statistik = []

    for kolom in kolom_analisis:

        data = df[kolom]

        rata_rata = data.mean()

        jumlah_kuadrat = ((data - rata_rata) ** 2).sum()

        standar_deviasi = data.std()

        minimum = data.min()

        maksimum = data.max()

        statistik.append({
            "variabel": kolom,
            "rata_rata": rata_rata,
            "jumlah_kuadrat": jumlah_kuadrat,
            "standar_deviasi": standar_deviasi,
            "minimum": minimum,
            "maksimum": maksimum
        })

    return render_template(
        "index.html",
        data=df.to_dict("records"),
        kolom=df.columns.tolist(),
        statistik=statistik
    )


if __name__ == "__main__":
    app.run(debug=True)