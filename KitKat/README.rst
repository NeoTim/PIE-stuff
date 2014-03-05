Analysis of KitKat binaries
===========================

Binaries are pulled from Moto G running KitKat 4.4.2


::

  $ sudo adb pull /system/bin bin
  $ sudo adb pull /system/lib lib

  $ checksec.py ./bin/vold
  ./bin/vold,NX=Enabled,CANARY=Enabled,RELRO=Partial,PIE=Enabled,RPATH=Disabled,RUNPATH=Disabled,FORTIFY=Enabled,CATEGORY=None,TEMPPATHS=None,DEPS=...

  $ checksec.py ./bin/getsebool
  ./bin/getsebool,NX=Enabled,CANARY=Enabled,RELRO=Partial,PIE=Enabled,RPATH=Disabled,RUNPATH=Disabled,FORTIFY=Enabled,CATEGORY=None,TEMPPATHS=None,DEPS=...

  $ checksec.py ./bin/dropboxd  # android binary :-)
  ./bin/dropboxd,NX=Enabled,CANARY=Enabled,RELRO=Partial,PIE=Enabled,RPATH=Disabled,RUNPATH=Disabled,FORTIFY=Disabled,CATEGORY=None,TEMPPATHS=None,DEPS=...

  $ checksec.py ~/.dropbox-dist/dropbox  # AMD64 binary, Dropbox 2.7.39 :-(
  /home/dkholia/.dropbox-dist/dropbox,NX=Enabled,CANARY=Enabled,RELRO=Disabled,PIE=Disabled,RPATH=Enabled,RUNPATH=Disabled,FORTIFY=Disabled,CATEGORY=network-ip,TEMPPATHS=None,DEPS=...

  $ sudo adb shell

  shell@falcon_umtsds:/ $ cat /proc/sys/kernel/randomize_va_space
  2

Links
=====

* https://jon.oberheide.org/blog/2012/02/27/aslr-in-android-ice-cream-sandwich-4-0/
