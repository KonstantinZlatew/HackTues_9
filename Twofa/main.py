import time
import qrcode
import pyotp

key = 'VikiZ'

uri = pyotp.totp.TOTP(key).provisioning_uri ( name = 'flask2fa',
                            issuer_name='secure_app')

print(uri)

qrcode.make(uri).save("qrcode.png")
