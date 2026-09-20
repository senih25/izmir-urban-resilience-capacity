from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
root=Path(r"C:\PROJELER\Izmir-Urban-Resilience-Atlas")
img=Image.new("RGB",(1900,400),"#073f32")
d=ImageDraw.Draw(img)
f1=ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf",60)
f2=ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf",29)
f3=ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf",36)
f4=ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf",21)
d.ellipse((1540,-260,2110,310),fill="#0b5b48")
d.text((70,52),"IZMIR URBAN RESILIENCE ATLAS",font=f1,fill="white")
d.text((72,132),"30 districts | population | transit | health | markets | emergency capacity",font=f2,fill="#b8f1da")
cards=[("4.50M","population"),("30","districts"),("2,382","assembly areas"),("867K","weekday departures")]
for i,(value,label) in enumerate(cards):
    x=72+i*390
    d.rounded_rectangle((x,215,x+365,330),radius=18,fill="#145a49",outline="#3b7b69",width=2)
    d.text((x+20,230),value,font=f3,fill="white")
    d.text((x+20,282),label,font=f4,fill="#d8eee7")
d.text((72,354),"Evidence-first capacity matrix | no composite district ranking",font=f4,fill="#b8cfc7")
out=root/"dataset-cover-image.png"
img.save(out,"PNG",optimize=True)
print("COVER_PASS",out.stat().st_size)
