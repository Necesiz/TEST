# Bu repo aykhan_s tərəfindən 29.11.2022 tarixində yığılıb
# Bu repodan icazəsiz hər hansı kodu sətri məlumatı 
# İcazəsiz kopyalıyan öz adına çıxaran işlədən peysərdi.

# t.me/RoBotlarimTg | YouTube: RoBotlarimTg |
# t.mr/aykhan_s | insta: aykhan026 | 



from komekci.aykhan import Nermin
from mesajlar.mesaj import salam, necesen, sagol, getdim, geldim, nermin, ban, start
from mesajlar.bot import yeni_user, start
from telethon import events, Button
import random


# Yeni istifadəçi mesajı
@Nermin.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"{random.choice(yeni_user)}")



@Nermin.on(events.NewMessage(pattern='(?i)/start+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(start)}")

@Nermin.on(events.NewMessage(pattern='(?i)salam+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(salam)}")

@Nermin.on(events.NewMessage(pattern='(?i)necəsən+'))
@Nermin.on(events.NewMessage(pattern='(?i)necesen+'))
@Nermin.on(events.NewMessage(pattern='(?i)nətərsən+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(necesen)}")

@Nermin.on(events.NewMessage(pattern='(?i)sağol+'))
@Nermin.on(events.NewMessage(pattern='(?i)sagol+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sagol)}")

@Nermin.on(events.NewMessage(pattern='(?i)getdim+'))
@Nermin.on(events.NewMessage(pattern='(?i)gedim+'))
@Nermin.on(events.NewMessage(pattern='(?i)gedirəm+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(getdim)}")

@Nermin.on(events.NewMessage(pattern='(?i)gəldim+'))
@Nermin.on(events.NewMessage(pattern='(?i)geldim+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(geldim)}")

@Nermin.on(events.NewMessage(pattern='(?i)nermin+'))
@Nermin.on(events.NewMessage(pattern='(?i)nərmin+'))
@Nermin.on(events.NewMessage(pattern='(?i)balam+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(nermin)}")

@Nermin.on(events.NewMessage(pattern='(?i)ban+'))
@Nermin.on(events.NewMessage(pattern='(?i)kick+'))
@Nermin.on(events.NewMessage(pattern='(?i)mute+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ban)}")



print(">> Nermin qoz kimi işləyir ♿ @RoBotlarimTg @aykhan_s <<")
Nermin.run_until_disconnected()
