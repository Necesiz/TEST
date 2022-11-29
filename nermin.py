# Bu repo aykhan_s tərəfindən 29.11.2022 tarixində yığılıb
# Bu repodan icazəsiz hər hansı kodu sətri məlumatı 
# İcazəsiz kopyalıyan öz adına çıxaran işlədən peysərdi.

# t.me/RoBotlarimTg | YouTube: RoBotlarimTg |
# t.mr/aykhan_s | insta: aykhan026 | 



from komekci.aykhan import Nermin
from mesajlar.mesaj import salam, necesen, sagol
from telethon import events, Button
import random


@Nermin.on(events.NewMessage)
async def yeni_mesaj(event: events.NewMessage.Event):
    mesaj = str(event.raw_text)
    if mesaj == f"{random.choice(salam)}":
      await event.reply(f"{random.choice(salam)}")

@Nermin.on(events.NewMessage)
async def yeni_mesaj(event: events.NewMessage.Event):
    mesaj = str(event.raw_text)
    if mesaj == "necəsən":
      await event.reply(f"{random.choice(necesen)}")

@Nermin.on(events.NewMessage)
async def yeni_mesaj(event: events.NewMessage.Event):
    mesaj = str(event.raw_text)
    if mesaj == "sağol":
      await event.reply(f"{random.choice(sagol)}")



print(">> Nermin qoz kimi işləyir ♿ @RoBotlarimTg @aykhan_s <<")
Nermin.run_until_disconnected()
