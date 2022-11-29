# Bu repo aykhan_s tərəfindən 29.11.2022 tarixində yığılıb
# Bu repodan icazəsiz hər hansı kodu sətri məlumatı 
# İcazəsiz kopyalıyan öz adına çıxaran işlədən peysərdi.

# t.me/RoBotlarimTg | YouTube: RoBotlarimTg |
# t.mr/aykhan_s | insta: aykhan026 | 



from komekci.aykhan import Nermin
from mesajlar import salam
from telethon import events, Button
import random


@Nermin.on(events.NewMessage)
async def yeni_mesaj(event: events.NewMessage.Event):
    mesaj = str(event.raw_text)
    if mesaj == "salam":
      await event.reply(f"{random.choice(salam)}")

print(">> Nermin qoz kimi işləyir ♿ @RoBotlarimTg @aykhan_s <<")
Nermin.run_until_disconnected()
