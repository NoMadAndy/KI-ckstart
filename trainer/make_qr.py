"""
QR-Codes für die Folien erzeugen (falls das Repo anders heißt oder die Umfrage-URL feststeht).

    pip install qrcode[pil]
    python trainer/make_qr.py https://codespaces.new/DEIN-USER/DEIN-REPO?quickstart=1 qr_codespaces.png
    python trainer/make_qr.py https://umfrage.deine-domain.tld qr_umfrage.png
"""
import sys
import qrcode

url, ziel = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "qr.png"
q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=2)
q.add_data(url)
q.make(fit=True)
q.make_image(fill_color="#1E1E24", back_color="white").save(ziel)
print(f"{ziel} für {url}")
