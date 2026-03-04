# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


s = "https://engineeringinkannada.in/"

url = pyqrcode.create(s)

url.svg("myqr.svg", scale = 8)

url.png('myqr.png',scale = 6 )