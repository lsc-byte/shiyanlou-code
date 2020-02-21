shiyanlou:~/ $ cd /home/shiyanlou/Code                               [21:47:59]
shiyanlou:Code/ $ git clone http://github.com/lsc-byte/shiyanlou-code.git
\u6b63\u514b\u9686\u5230 'shiyanlou-code'...
warning: \u60a8\u4f3c\u4e4e\u514b\u9686\u4e86\u4e00\u4e2a\u7a7a\u4ed3\u5e93\u3002
\u68c0\u67e5\u8fde\u63a5... \u5b8c\u6210\u3002
shiyanlou:Code/ $ ls                                                 [21:49:49]
shiyanlou-code
shiyanlou:Code/ $ cd shiyanlou-code                                  [21:50:03]
shiyanlou:shiyanlou-code/ (master) $                                 [21:50:19]
shiyanlou:shiyanlou-code/ (master) $ gedit jump7.py                  [21:55:36]

(gedit:278): GVFS-RemoteVolumeMonitor-WARNING **: remote volume monitor with dbus name org.gtk.vfs.UDisks2VolumeMonitor is not supported

(gedit:278): Gtk-WARNING **: Calling Inhibit failed: GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown: The name org.gnome.SessionManager was not provided by any .service files
shiyanlou:shiyanlou-code/ (master*) $ git init                       [21:57:02]
\u91cd\u65b0\u521d\u59cb\u5316\u73b0\u5b58\u7684 Git \u4ed3\u5e93\u4e8e /home/shiyanlou/Code/shiyanlou-code/.git/
shiyanlou:shiyanlou-code/ (master*) $ git add jump7.py               [21:57:17]
shiyanlou:shiyanlou-code/ (master*) $ ls                             [21:57:28]
jump7.py
shiyanlou:shiyanlou-code/ (master*) $ git config --global user.name'lsc'
shiyanlou:shiyanlou-code/ (master*) $ git config --global user.email'123@123.com'
shiyanlou:shiyanlou-code/ (master*) $ git commit -m 'daima'          [21:58:27]

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: empty ident name (for <shiyanlou@f8776fbde792.(none)>) not allowed
shiyanlou:shiyanlou-code/ (master*) $ git config --global user.email '123@123.com'
shiyanlou:shiyanlou-code/ (master*) $ git config --global user.name 'lsc'
shiyanlou:shiyanlou-code/ (master*) $ git commit -m 'daima'          [21:59:21]
[master \uff08\u6839\u63d0\u4ea4\uff09 6ef4e49] daima
 1 file changed, 14 insertions(+)
 create mode 100644 jump7.py
shiyanlou:shiyanlou-code/ (master) $ git remote add origin https://github.com/lsc-byte/shiyanlou-code.git
fatal: \u8fdc\u7a0b origin \u5df2\u7ecf\u5b58\u5728\u3002
shiyanlou:shiyanlou-code/ (master) $ git remote add origin1 https://github.com/lsc-byte/shiyanlou-code.git
shiyanlou:shiyanlou-code/ (master) $ git push origin1 master         [22:00:39]
Username for 'https://github.com': lsc-byte
Password for 'https://lsc-byte@github.com': 
\u5bf9\u8c61\u8ba1\u6570\u4e2d: 3, \u5b8c\u6210.
Delta compression using up to 4 threads.
\u538b\u7f29\u5bf9\u8c61\u4e2d: 100% (2/2), \u5b8c\u6210.
\u5199\u5165\u5bf9\u8c61\u4e2d: 100% (3/3), 447 bytes | 0 bytes/s, \u5b8c\u6210.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/lsc-byte/shiyanlou-code.git
 * [new branch]      master -> master
