#!/usr/bin/env python
#encoding:utf-8

import jwt, datetime,hashlib

class AuthToken:
    def __init__(self,token_secret='3AIiOq18i~H=WWTIGq4ODQyMzcsIdfghs'):
        self.token_secret = token_secret

    def encode_auth_token(self, **kargs):
        """
        生成认证Token
        :param user_id: string
        :param username: string
        :param nickname: string
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=10),
                'nbf': datetime.datetime.utcnow() - datetime.timedelta(seconds=10),
                'iat': datetime.datetime.utcnow(),
                'sub': 'my token',
                'data': {
                    'id': kargs.get('id'),
                    'username': kargs.get('username'),
                    'nickname': kargs.get('nickname'),
                    'superuser': kargs.get('superuser', False)
                }
            }
            return jwt.encode(
                payload,
                self.token_secret,
                algorithm='HS256'
            )

        except Exception as e:
            return e

    def decode_auth_token(self, auth_token):
        """
         验证Token
        :param auth_token:
        :return: dict
        """
        try:
            payload = jwt.decode(auth_token, self.token_secret, algorithms=['HS256'],
                                 leeway=datetime.timedelta(seconds=10))
            if 'data' in payload and 'user_id' in payload['data']:
                return payload['data']
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return dict(status=-1, msg='Token过期')
        except jwt.InvalidTokenError:
            return dict(status=-2, msg='无效Token')

def gen_md5(pd):
    m2 = hashlib.md5()
    m2.update(pd.encode("utf-8"))
    return m2.hexdigest()