# -*- coding: utf-8 -*-

from pybd_decrypt.data import decrypt


class TestDataDecryptCommands(object):

    def test_decrypt(self):
        sessionKey = '5c58679ff3d0e992de6338cf0c2944d7'
        encryptedData = '2e1xg4uFtsWLRoYMT9H398Zb1wfXxtl9Or9Q39Qb5JXiYp4ARCwGktdF+cpQC5GhRMXc8Eun9c9Hws2KCmxTi+/QZN9lQhCwWdkrdRXmQeqDAmih0Zng2nM90FlIbEFDPchGuehiVZ4RxSbJnpa1BPSU3F4KLLUTsX+jAZxdulP3sczsN30XpjDf48m3C3Ff/5Rkg3/Q3MhlQEF9lTSL7fdiGgvVHaEav5Fr7hRNqG3G/S8a+WMNX9R3cmdf05sTt+GAvPft0tgTzs7sl15d/g=='
        iv = '5c58679ff3d0e992de633w=='
        result = decrypt(sessionKey=sessionKey, encryptedData=encryptedData, iv=iv)
        # {u'headimgurl': u'https://himg.bdimg.com/sys/portrait/item/ea8348514d4953970a',
        #  u'nickname': u'HQMIS',
        #  u'openid': u'mgJNc4Ut1tzE1L1ltQCCBWCZ9L',
        #  u'sex': 1}
        assert isinstance(result, dict)
        assert result['nickname'] == 'HQMIS'
