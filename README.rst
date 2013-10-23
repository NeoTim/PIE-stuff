Why PIE?
========

On OS X (and iOS), processes running position-independent executables have
varying levels of ASLR protection depending on the OS release. The main
executable's load address, shared library load addresses, and the heap and
stack base addresses may be randomized. Position-independent executables are
produced by supplying the -pie flag to the linker (or defeated by supplying
-no_pie). iOS 4.3 or later, and OS X 10.7 or later, fully support PIE
executables; moreover, applications submitted for distribution via Apple's App
Store are required to be fully position-independent, see [1] for more details.

BlackBerry SDK tools enable PIE by default for new projects, see [3] and [4]
for details.

Starting with Android 4.1, Google is forcing "full ASLR" (PIE) to overcome
common security exploits, see [5] and [6] for more details.

In OpenBSD, the amd64 and other platforms have been switched to PIE
(position-independent executables) by *default*.

Google Chrome and Opera binaries for Linux are already PIE. Firefox folks
are already looking at support and / or enabling PIE.

Notes
=====

In addition to being the default on OS X, PIE is compulsorily *required* even
for iOS apps to be "approved".

If Apple can enable PIE (by default) on its "consumer-grade" products, I
believe that we can do a bit better.

Even on Apple mobile phones, which are limited CPU and battery wise, PIE is
*compulsorily* required for *everything*.

Mach-O executables scanner
==========================

::

   $ python mach_o_flags.py --show mavericks/zsh  # works everywhere!
   [+] PIE is ON
   [-] Heap Safety is OFF

   $ otool -hv /bin/ls  # works only on OS X
   /bin/ls:
   Mach header
         magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
   MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    19       1816   NOUNDEFS DYLDLINK TWOLEVEL PIE

Rants
=====

* It seems that Apple engineers still don't know that `stderr` exists. Maybe
  they will figure it out in the coming time.

References
==========

[1] `Position-independent executables <http://en.wikipedia.org/wiki/Position-independent_code#Position-independent_executables>`_

[2] `Apple - Building a Position Independent Executable <https://developer.apple.com/library/ios/qa/qa1788/_index.html>`_

[3] `BlackBerry - Compile with security options <http://developer.blackberry.com/native/documentation/core/com.qnx.doc.ide.userguide/topic/bb_tablet_compile_security_options.html>`_

[4] `BlackBerry - Using compiler and linker defenses <http://developer.blackberry.com/playbook/native/documentation/com.qnx.doc.native_sdk.security/topic/using_compiler_linker_defenses.html>`_

[5] `Android - PIE <http://stackoverflow.com/questions/14990461/why-does-arm-linux-androideabi-gcc-enforce-fpic>`_

[6] `Exploit Mitigations in Android Jelly Bean 4.1 <https://blog.duosecurity.com/2012/07/exploit-mitigations-in-android-jelly-bean-4-1/>`_

Credits
=======

* Lot of the text in this article is borrowed from the `change_mach_o_flags.py <http://src.chromium.org/svn/trunk/src/build/mac/change_mach_o_flags.py>`_ script.
