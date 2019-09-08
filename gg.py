import os, sys
print '\x1b[1;32mSilahkan Masukkan Username & Password tools ini'
print '\x1b[1;32matau silahkan Hubungi  085691015635 '
print '\x1b[1;32mScript MR.BLACK0304 '
username = 'BOCIL'
password = 'N00B'

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


def main():
    uname = raw_input('username : ')
    if uname == username:
        pwd = raw_input('password : ')
        if pwd == password:
            print '\x1b[1;32mAlhmdllh sudah masuk juga..',
            sys.exit()
        else:
            print '\x1b[1;32mMaaf Masukkan password Anda salah... [?]\x1b[00m'
            print 'Silahkan segera log-in kembali...!!\n'
            restart()
    else:
        print '\x1b[1;32mMaaf Masukkan Username Anda salah... [?]\x1b[00m'
        print 'Silahkan segera log-in kembali...!!\n'
        restart()


try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    restart()<uncompyle6.semantics.pysource.SourceWalker object at 0x7fe14c6d0ad0>
