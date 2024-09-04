import qrcode

img = qrcode.make("https://kissasiantv.cx/drama/got-a-crush-on-you-2023-episode-1")

img.save("qr.png", "PNG")