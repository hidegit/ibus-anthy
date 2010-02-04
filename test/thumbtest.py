# -*- coding: utf-8 -*-

import gtk
import gobject

from ibus import keysyms, modifier
#['copy', 'free', 'get_axis', 'get_coords', 'get_root_coords', 'get_screen', 'get_state', 'get_time', 'group', 'hardware_keycode', 'keyval', 'put', 'send_client_message', 'send_clientmessage_toall', 'send_event', 'set_screen', 'state', 'string', 'time', 'type', 'window']

_table = {
    'q': [u'。', u'',   u'ぁ'],
    'w': [u'か', u'が', u'え'],
    'e': [u'た', u'だ', u'り'],
    'r': [u'こ', u'ご', u'ゃ'],
    't': [u'さ', u'ざ', u'れ'],

    'y': [u'ら', u'よ', u'ぱ'],
    'u': [u'ち', u'に', u'ぢ'],
    'i': [u'く', u'る', u'ぐ'],
    'o': [u'つ', u'ま', u'づ'],
    'p': [u'，',  u'ぇ', u'ぴ'],
    '@': [u'、', u'',   u''],
    '[': [u'゛', u'゜', u''],

    'a': [u'う', u'ヴ',   u'を'],
    's': [u'し', u'じ', u'あ'],
    'd': [u'て', u'で', u'な'],
    'f': [u'け', u'げ', u'ゅ'],
    'g': [u'せ', u'ぜ', u'も'],

    'h': [u'は', u'み', u'ば'],
    'j': [u'と', u'お', u'ど'],
    'k': [u'き', u'の', u'ぎ'],
    'l': [u'い', u'ょ', u'ぽ'],
    ';': [u'ん', u'っ', u''],

    'z': [u'．',  u'',   u'ぅ'],
    'x': [u'ひ', u'び', u'ー'],
    'c': [u'す', u'ず', u'ろ'],
    'v': [u'ふ', u'ぶ', u'や'],
    'b': [u'へ', u'べ', u'ぃ'],

    'n': [u'め', u'ぬ', u'ぷ'],
    'm': [u'そ', u'ゆ', u'ぞ'],
    ',': [u'ね', u'む', u'ぺ'],
    '.': [u'ほ', u'わ', u'ぼ'],
    '/': [u'・', u'ぉ', u''],

    '1': [u'1',  u'？',   u'？'],
    '2': [u'2',  u'／',   u'／'],
    '3': [u'3',  u'～',   u'～'],
    '4': [u'4',  u'「',   u'「'],
    '5': [u'5',  u'」',   u'」'],

    '6': [u'6',  u'［',  u'［'],
    '7': [u'7',  u'］',  u'］'],
    '8': [u'8',  u'（',  u'（'],
    '9': [u'9',  u'）',  u'）'],
    '0': [u'0',  u'『',  u'『'],
    '-': [u'-',  u'』',  u'』'],
}

_shift_table = {
    'H': u'ぱ',
    'X': u'ぴ',
    'V': u'ぷ',
    'B': u'ぺ',
    '>': u'ぽ',
}

table = {}
for k in _table.keys():
    table[ord(k)] = _table[k]

shift_table = {}
for k in _shift_table.keys():
    shift_table[ord(k)] = _shift_table[k]

NICOLA_J = table

NICOLA_F = NICOLA_J.copy()
NICOLA_F.update({ord(':'): [u'、', u'', u'']})
del(NICOLA_F[ord('@')])

NICOLA_A = NICOLA_J.copy()
NICOLA_A.update({
    ord('9'): [u'9', u'（', u'（'],
    ord('0'): [u'0', u'）', u'）'],
    ord('-'): [u'=',  u'『',  u'『'],
    ord('='): [u'-',  u'』',  u'』'],
    ord('['): [u'、', u'', u''],
    ord(']'): [u'゛', u'゜', u'']
})
del(NICOLA_A[ord('8')])
del(NICOLA_A[ord('@')])

class thumb:
    table = NICOLA_J
    shift_table = shift_table
    RS = keysyms.Henkan
    LS = keysyms.Muhenkan
    RS = keysyms.space
    LS = keysyms.Super_L
    T1 = 100
    T2 = 75

class DummyEngine:
    def __init__(self):
        self._MM = 0
        self._SS = 0
        self._H = None

    def process_key_event_thumb(self, keyval, keycode, state):
#        import gtk
#        import thumb

        def on_timeout(keyval):
            if self._MM:
                print '\t0_1'
                insert(thumb.table[self._MM][self._SS])
            else:
                print '\t0_2'
                cmd_exec([0, RS(), LS()][self._SS])
            self._H = None

        def start(t):
            self._H = gobject.timeout_add(t, on_timeout, keyval)

        def stop():
            if self._H:
                gobject.source_remove(self._H)
                self._H = None
                return True
            return False

        def insert(keyval):
            print 'INSERT\t%s' % keyval
            return True
            '''try:
                ret = self.__on_key_common(ord(keyval))
                if (keyval in u',.、。' and
                    self.__prefs.get_value('common', 'behavior_on_period')):
                    return self.__cmd_convert(keyval, state)
                return ret
            except:
                pass'''

        def cmd_exec(keyval, state=0):
            print 'CMD_EXEC'
            return False
            '''key = self._mk_key(keyval, state)
            for cmd in self.__keybind.get(key, []):
                print 'cmd =', cmd
                try:
                    if getattr(self, cmd)(keyval, state):
                        return True
                except:
                    print >> sys.stderr, 'Unknow command = %s' % cmd
            return False'''

        def RS():
#            return self.__prefs.get_value('common', 'thumb_rs')
            return thumb.RS

        def LS():
#            return self.__prefs.get_value('common', 'thumb_ls')
            return thumb.LS

        def T1():
#            return self.__prefs.get_value('common', 'thumb_t1')
            return thumb.T1

        def T2():
#            return self.__prefs.get_value('common', 'thumb_t2')
            return thumb.T2

        print 'keyval = %s, keycode = %d, state = %08x' % (
                    keysyms.keycode_to_name(keyval), keycode, state),
        print 'MM = %s, SS = %d' % (keysyms.keycode_to_name(self._MM), self._SS)

        state = state & (modifier.SHIFT_MASK |
                         modifier.CONTROL_MASK |
                         modifier.MOD1_MASK |
                         modifier.RELEASE_MASK)

#        if keyval in KP_Table and self.__prefs.get_value('common',
#                                                         'ten_key_mode'):
#            keyval = KP_Table[keyval]

        if state & modifier.RELEASE_MASK:
            if keyval == self._MM:
                print '\t1_1'
                if stop():
                    insert(thumb.table[self._MM][self._SS])
                self._MM = 0
            elif (1 if keyval == RS() else 2) == self._SS:
                print '\t1_2'
                if stop():
                    cmd_exec([0, RS(), LS()][self._SS])
                self._SS = 0
            else:
                print '\t1_3'
        else:
            if keyval in [LS(), RS()] and state == 0:
                if self._SS:
                    print '\t2_1_1'
                    stop()
                    cmd_exec([0, RS(), LS()][self._SS])
                    self._SS = 1 if keyval == RS() else 2
                    start(T1())
                elif self._MM:
                    print '\t2_1_2'
                    stop()
                    insert(thumb.table[self._MM][1 if keyval == RS() else 2])
                else:
                    print '\t2_1_3'
                    self._SS = 1 if keyval == RS() else 2
                    start(T1())
            elif keyval in thumb.table.keys() and state == 0:
                if self._MM:
                    print '\t2_2_2'
                    stop()
                    insert(thumb.table[self._MM][self._SS])
                    start(T2())
                    self._MM = keyval
                elif self._SS:
                    print '\t2_2_1'
                    stop()
                    insert(thumb.table[keyval][self._SS])
                else:
                    print '\t2_2_3'
                    if cmd_exec(keyval, state):
                        return True
                    start(T2())
                    self._MM = keyval
            else:
                if self._MM:
                    print '\t2_3_1'
                    stop()
                    insert(thumb.table[self._MM][self._SS])
                elif self._SS:
                    print '\t2_3_2'
                    stop()
                    cmd_exec([0, RS(), LS()][self._SS])
                if cmd_exec(keyval, state):
                    print '\t2_3_3'
                    return True
                elif 0x21 <= keyval <= 0x7e and state & (modifier.CONTROL_MASK | modifier.MOD1_MASK) == 0:
                    insert(thumb.shift_table.get(keyval, unichr(keyval)))
                    print '\t2_3_4'
                else:
                    print '\t2_3_5'
#                    if not self.__preedit_ja_string.is_empty():
#                        return True
#                    return False
        return True


if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 2:
        if sys.argv[1].upper() == 'NICOLA_F':
            thumb.table = NICOLA_F
        elif sys.argv[1].upper() == 'NICOLA_A':
            thumb.table = NICOLA_A
            thumb.RS = keysyms.space
            thumb.LS = keysyms.Super_L

    engine = DummyEngine()

    def press(w, e):
        print 'PRESS:\ttime =', e.time,
        engine.process_key_event_thumb(e.keyval, e.hardware_keycode, e.state)
        print
        return True

    def release(w, e):
        print 'RELEASE:time =', e.time,
        engine.process_key_event_thumb(e.keyval, e.hardware_keycode,
                                       e.state | modifier.RELEASE_MASK)
        print
        return True

    for tbl in [NICOLA_J, NICOLA_F, NICOLA_A]:
        for s in '890-=@:[]':
            try:
                a, b, c = tbl[ord(s)]
                print s, a, b, c
            except:
                print 'error', s
        print
    
    w = gtk.Window()
    w.connect('destroy', gtk.main_quit)
    w.connect('key-press-event', press)
    w.connect('key-release-event', release)
    w.show()

    gtk.main()
