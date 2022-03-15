from InterConnect import send_cmd
from Debug import errlog_add


def sendcmd(*args, **kwargs):

    def __send(_host, _cmd):
        try:
            out = send_cmd(_host, _cmd)
        except Exception as e:
            out = []
            errlog_add('[intercon] sendcmd: {}'.format(e))
        return out

    host = kwargs.get('host', None)
    cmd = kwargs.get('cmd', None)

    # Host correction if keyword-arg 'host' was not found
    if host is None:
        host = args[0]
        args = args[1:]

    # Cmd correction if keyword-arg was not found
    if cmd is None:
        cmd = ' '.join([k.replace(',', '') for k in args])
        return __send(host, cmd)
    cmd = ''.join([k.replace(',', '') for k in cmd])
    return __send(host, cmd)


#######################
# LM helper functions #
#######################

def help():
    return 'sendcmd "hello" host="IP/hostname") OR sendcmd host="IP/hostname" cmd="system rssi")', \
           'example: intercon sendcmd "10.0.1.84" "system rssi" OR intercon sendcmd "system rssi" host="node01.local"'