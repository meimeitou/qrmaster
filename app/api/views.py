import cv2
import numpy as np


def qrdecode(filedata: bytes) -> str:
    img = np.asarray(bytearray(filedata), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    qrCodeDetector = cv2.QRCodeDetector()
    decodedText, points, _ = qrCodeDetector.detectAndDecode(img)
    if points is None:
        return "二维码识别失败"
    return decodedText

def qrencode()->bytes:
    pass