from flask import Blueprint, send_file,request
from utils.format import err_msg,ok_msg_with
from .views import qrdecode

api = Blueprint(
    'api',
    __name__,
    template_folder='templates',
    url_prefix="/api",
    static_folder='static')


@api.route('/ping', methods=['POST', 'GET'])
def ping():
    '''
    ping
    '''
    return "Pong"

@api.route('/qrdecode', methods=['POST', 'GET'])
def decode():
    '''
    decode qr
    '''
    if 'file' not in request.files:
        return err_msg("400", "no image file")
    file = request.files['file']
    return ok_msg_with(qrdecode(file.read()))
