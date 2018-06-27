%define keepstatic 1
Name     : sof-crosstool-ng
Version  : c7.3
Release  : 1
URL      : https://github.com/thesofproject/crosstool-ng/archive/sof-gcc7.3.tar.gz
Source0  : https://github.com/thesofproject/crosstool-ng/archive/sof-gcc7.3.tar.gz
Source1  : http://isl.gforge.inria.fr/isl-0.19.tar.xz
Source2  : https://ftpmirror.gnu.org/gnu/binutils/binutils-2.30.tar.xz
Source3  : https://ftpmirror.gnu.org/gnu/gcc/gcc-8.1.0/gcc-8.1.0.tar.xz
Source4  : https://github.com/thesofproject/xtensa-overlay/archive/sof-v1.2-gcc8.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 GFDL-1.2 GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: sof-crosstool-ng-bin
Requires: sof-crosstool-ng-data
BuildRequires : autogen
BuildRequires : bison
BuildRequires : bzip2
BuildRequires : curl-dev
BuildRequires : dejagnu
BuildRequires : docbook-xml docbook-utils doxygen
BuildRequires : expect
BuildRequires : flex
BuildRequires : gdb-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev
BuildRequires : gmp-dev
BuildRequires : gperf
BuildRequires : graphviz
BuildRequires : grep
BuildRequires : guile
BuildRequires : gzip
BuildRequires : help2man
BuildRequires : libstdc++
BuildRequires : libunwind-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : mpc-dev
BuildRequires : mpfr-dev
BuildRequires : ncurses ncurses-dev ncurses-lib
BuildRequires : pkgconfig(zlib)
BuildRequires : procps-ng
BuildRequires : sed
BuildRequires : tar
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : valgrind-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-packages-gdb-8.1-fix-build-and-include-stdint.h.patch
Patch2: 0002-config-apl-gcc8.1-gdb8.1-and-binutils-2.30.patch
Patch3: 0003-support-mockbuild.patch

%description
These autoconf helper macros come from various sources:
- ax_*.m4: autoconf-archive, version 2017.09.28 (copied)
- pkg.m4: pkg-config, version 0.29.2 (run configure, then copy)
- gettext.m4, iconv.m4, intlmacosx.m4, nls.m4: gettext 0.19.8
- ctng_*.m4: obviously, implemented anew
- po.m4: a local dummy stub for gettext's version

%package bin
Summary: bin components for the sof-crosstool-ng package.
Group: Binaries
Requires: sof-crosstool-ng-data

%description bin
bin components for the sof-crosstool-ng package.


%package data
Summary: data components for the sof-crosstool-ng package.
Group: Data

%description data
data components for the sof-crosstool-ng package.


%package dev
Summary: dev components for the sof-crosstool-ng package.
Group: Development
Requires: sof-crosstool-ng-bin
Requires: sof-crosstool-ng-data
Provides: sof-crosstool-ng-devel

%description dev
dev components for the sof-crosstool-ng package.


%prep
tar -xf %{SOURCE4}
tar -xf %{SOURCE1}
tar -xf %{SOURCE2}
tar -xf %{SOURCE3}
cd ..
%setup -q -n crosstool-ng-sof-gcc7.3
mkdir -p %{_topdir}/BUILD/crosstool-ng-sof-gcc7.3/../xtensa-overlay
mv %{_topdir}/BUILD/xtensa-overlay-sof-v1.2-gcc8.1/* %{_topdir}/BUILD/crosstool-ng-sof-gcc7.3/../xtensa-overlay
mkdir -p %{_topdir}/BUILD/crosstool-ng-sof-gcc7.3/../isl
mv %{_topdir}/BUILD/isl-0.19/* %{_topdir}/BUILD/crosstool-ng-sof-gcc7.3/../isl
mkdir -p %{_topdir}/BUILD/crosstool-ng-sof-gcc7.3/../binutils
mv %{_topdir}/BUILD/binutils-2.30/* %{_topdir}/BUILD/crosstool-ng-sof-gcc7.3/../binutils
mkdir -p %{_topdir}/BUILD/crosstool-ng-sof-gcc7.3/../gcc
mv %{_topdir}/BUILD/gcc-8.1.0/* %{_topdir}/BUILD/crosstool-ng-sof-gcc7.3/../gcc
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530518798
pushd mockbuild/
%configure
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1530518798
rm -rf %{buildroot}
pushd mockbuild/
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xtensa-apl-elf-addr2line
/usr/bin/xtensa-apl-elf-ar
/usr/bin/xtensa-apl-elf-as
/usr/bin/xtensa-apl-elf-c++filt
/usr/bin/xtensa-apl-elf-cc
/usr/bin/xtensa-apl-elf-cpp
/usr/bin/xtensa-apl-elf-ct-ng.config
/usr/bin/xtensa-apl-elf-elfedit
/usr/bin/xtensa-apl-elf-gcc
/usr/bin/xtensa-apl-elf-gcc-8.1.0
/usr/bin/xtensa-apl-elf-gcc-ar
/usr/bin/xtensa-apl-elf-gcc-nm
/usr/bin/xtensa-apl-elf-gcc-ranlib
/usr/bin/xtensa-apl-elf-gcov
/usr/bin/xtensa-apl-elf-gcov-dump
/usr/bin/xtensa-apl-elf-gcov-tool
/usr/bin/xtensa-apl-elf-gprof
/usr/bin/xtensa-apl-elf-ld
/usr/bin/xtensa-apl-elf-ld.bfd
/usr/bin/xtensa-apl-elf-nm
/usr/bin/xtensa-apl-elf-objcopy
/usr/bin/xtensa-apl-elf-objdump
/usr/bin/xtensa-apl-elf-ranlib
/usr/bin/xtensa-apl-elf-readelf
/usr/bin/xtensa-apl-elf-size
/usr/bin/xtensa-apl-elf-strings
/usr/bin/xtensa-apl-elf-strip

%files data
%defattr(-,root,root,-)
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-addr2line
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-ar
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-as
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-c++filt
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-cc
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-cpp
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-ct-ng.config
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-elfedit
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-gcc
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-gcc-8.1.0
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-gcc-ar
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-gcc-nm
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-gcc-ranlib
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-gcov
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-gcov-dump
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-gcov-tool
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-gprof
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-ld
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-ld.bfd
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-nm
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-objcopy
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-objdump
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-ranlib
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-readelf
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-size
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-strings
/usr/share/xtensa-apl-elf/bin/xtensa-apl-elf-strip
/usr/share/xtensa-apl-elf/build.log.bz2
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/crtbegin.o
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/crtend.o
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/crti.o
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/crtn.o
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include-fixed/README
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include-fixed/limits.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include-fixed/syslimits.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/install-tools/fixinc_list
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/install-tools/gsyslimits.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/install-tools/include/README
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/install-tools/macro_list
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/install-tools/mkheaders.conf
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/libgcc.a
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/libgcov.a
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/gtype.state
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ada/gcc-interface/ada-tree.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/all-tree.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/b-header-vars
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/brig-builtins.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/builtin-attrs.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/builtin-types.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/builtins.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/c-family/c-common.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cfg-flags.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/chkp-builtins.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cif-code.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cp/cp-tree.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/dbgcnt.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/diagnostic.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gcov-counter.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gsstruct.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gtm-builtins.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hsa-builtins.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/insn-notes.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/internal-fn.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/machmode.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/mode-classes.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/objc/objc-tree.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/omp-builtins.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/optabs.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/params.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/params.list
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/pass-instances.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/passes.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/plugin.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/predict.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/reg-notes.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/rtl.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/sanitizer.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/stab.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/sync-builtins.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/target-insns.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/target.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/timevar.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/treestruct.def
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/libcc1plugin.so
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/libcc1plugin.so.0
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/libcc1plugin.so.0.0.0
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/libcp1plugin.so
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/libcp1plugin.so.0
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/libcp1plugin.so.0.0.0
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.x
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xbn
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xc
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xce
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xd
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xdc
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xdce
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xde
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xdw
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xdwe
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xe
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xn
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xr
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xs
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xsc
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xsce
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xse
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xsw
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xswe
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xu
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xw
/usr/share/xtensa-apl-elf/lib/ldscripts/elf32xtensa.xwe
/usr/share/xtensa-apl-elf/lib64/libcc1.so
/usr/share/xtensa-apl-elf/lib64/libcc1.so.0
/usr/share/xtensa-apl-elf/lib64/libcc1.so.0.0.0
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/cc1
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/collect2
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/install-tools/fixinc.sh
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/install-tools/fixincl
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/install-tools/mkheaders
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/install-tools/mkinstalldirs
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/liblto_plugin.so
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/liblto_plugin.so.0
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/liblto_plugin.so.0.0.0
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/lto-wrapper
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/lto1
/usr/share/xtensa-apl-elf/libexec/gcc/xtensa-apl-elf/8.1.0/plugin/gengtype
/usr/share/xtensa-apl-elf/xtensa-apl-elf/bin/ar
/usr/share/xtensa-apl-elf/xtensa-apl-elf/bin/as
/usr/share/xtensa-apl-elf/xtensa-apl-elf/bin/ld
/usr/share/xtensa-apl-elf/xtensa-apl-elf/bin/ld.bfd
/usr/share/xtensa-apl-elf/xtensa-apl-elf/bin/nm
/usr/share/xtensa-apl-elf/xtensa-apl-elf/bin/objcopy
/usr/share/xtensa-apl-elf/xtensa-apl-elf/bin/objdump
/usr/share/xtensa-apl-elf/xtensa-apl-elf/bin/ranlib
/usr/share/xtensa-apl-elf/xtensa-apl-elf/bin/readelf
/usr/share/xtensa-apl-elf/xtensa-apl-elf/bin/strip
/usr/share/xtensa-apl-elf/xtensa-apl-elf/sys-include/COPIED

%files dev
%defattr(-,root,root,-)
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/float.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/gcov.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/iso646.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/stdalign.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/stdarg.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/stdatomic.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/stdbool.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/stddef.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/stdfix.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/stdint-gcc.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/stdint.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/stdnoreturn.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/tgmath.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/unwind.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/include/varargs.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/install-tools/include/limits.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/addresses.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/alias.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/alloc-pool.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ansidecl.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/asan.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/attribs.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/auto-host.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/auto-profile.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/backend.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/basic-block.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/bb-reorder.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/bitmap.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/builtins.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/bversion.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/c-family/c-common.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/c-family/c-objc.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/c-family/c-pragma.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/c-family/c-pretty-print.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/c-tree.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/calls.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ccmp.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cfg.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cfganal.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cfgbuild.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cfgcleanup.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cfgexpand.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cfghooks.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cfgloop.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cfgloopmanip.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cfgrtl.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cgraph.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/collect-utils.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/collect2-aix.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/collect2.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/color-macros.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/conditions.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/config.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/config/dbxelf.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/config/elfos.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/config/initfini-array.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/config/newlib-stdint.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/config/xtensa/elf.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/config/xtensa/xtensa-protos.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/config/xtensa/xtensa.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/configargs.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/context.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/convert.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/coretypes.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/coverage.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cppbuiltin.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cppdefault.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cpplib.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/cselib.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/data-streamer.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/dbgcnt.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/dbxout.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/dce.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ddg.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/debug.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/defaults.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/df.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/dfp.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/diagnostic-color.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/diagnostic-core.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/diagnostic.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/dojump.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/dominance.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/domwalk.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/double-int.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/dumpfile.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/dwarf2asm.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/dwarf2out.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/edit-context.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/emit-rtl.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/errors.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/et-forest.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/except.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/explow.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/expmed.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/expr.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/fibonacci_heap.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/file-find.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/file-prefix-map.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/filenames.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/fixed-value.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/flag-types.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/flags.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/fold-const-call.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/fold-const.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/function.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gcc-plugin.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gcc-rich-location.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gcc-symtab.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gcc.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gcov-io.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gcse-common.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gcse.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/generic-match.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gengtype.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/genrtl.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gensupport.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ggc-internal.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ggc.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-builder.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-expr.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-fold.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-iterator.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-low.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-match.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-predict.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-pretty-print.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-ssa-evrp-analyze.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-ssa-warn-restrict.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-ssa.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-streamer.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple-walk.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimple.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimplify-me.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gimplify.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/glimits.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/graph.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/graphds.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/graphite.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gstab.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gsyms.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gsyslimits.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/gtype-desc.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hard-reg-set.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hash-map-traits.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hash-map.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hash-set.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hash-table.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hash-traits.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hashtab.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/highlev-plugin-common.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hooks.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hosthooks-def.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hosthooks.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hsa-brig-format.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hsa-common.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hw-doloop.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/hwint.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ifcvt.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/inchash.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/incpath.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/input.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/insn-addr.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/insn-codes.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/insn-constants.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/insn-flags.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/insn-modes-inline.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/insn-modes.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/int-vector-builder.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/internal-fn.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/intl.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-chkp.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-fnsummary.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-icf-gimple.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-icf.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-inline.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-param-manipulation.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-predicate.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-prop.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-ref.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-reference.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ipa-utils.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ira-int.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ira.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/is-a.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/langhooks-def.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/langhooks.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/lcm.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/libfuncs.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/libiberty.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/limitx.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/limity.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/line-map.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/loop-unroll.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/lower-subreg.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/lra-int.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/lra.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/lto-compress.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/lto-section-names.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/lto-streamer.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/machmode.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/md5.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/mem-stats-traits.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/mem-stats.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/memmodel.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/memory-block.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/obstack.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/omp-expand.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/omp-general.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/omp-grid.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/omp-low.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/omp-offload.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/omp-simd-clone.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/optabs-libfuncs.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/optabs-query.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/optabs-tree.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/optabs.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/options.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/opts-diagnostic.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/opts.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/output.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/params-enum.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/params-list.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/params-options.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/params.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/pass_manager.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/plugin-api.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/plugin-version.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/plugin.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/poly-int-types.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/poly-int.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/predict.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/prefix.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/pretty-print.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/print-rtl.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/print-tree.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/profile-count.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/profile.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/read-md.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/read-rtl-function.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/real.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/realmpfr.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/recog.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/regcprop.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/regrename.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/regs.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/regset.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/reload.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/resource.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/rtl-chkp.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/rtl-error.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/rtl-iter.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/rtl.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/rtlhash.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/rtlhooks-def.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/rtx-vector-builder.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/run-rtl-passes.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/safe-ctype.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/sbitmap.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/sched-int.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/sel-sched-dump.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/sel-sched-ir.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/sel-sched.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/selftest-diagnostic.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/selftest-rtl.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/selftest.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/sese.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/shrink-wrap.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/signop.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/sparseset.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/spellcheck-tree.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/spellcheck.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/splay-tree.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/sreal.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ssa-iterators.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ssa.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/statistics.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/stmt.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/stor-layout.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/streamer-hooks.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/stringpool.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/substring-locations.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/symbol-summary.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/symtab.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/system.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/target-def.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/target-globals.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/target-hooks-macros.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/target.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/targhooks.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/timevar.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tm-preds.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tm.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tm_p.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/toplev.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tracer.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/trans-mem.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-affine.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-cfg.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-cfgcleanup.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-check.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-chkp.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-chrec.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-core.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-data-ref.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-dfa.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-diagnostic.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-dump.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-eh.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-hash-traits.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-hasher.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-if-conv.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-inline.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-into-ssa.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-iterator.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-nested.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-object-size.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-outof-ssa.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-parloops.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-pass.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-phinodes.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-pretty-print.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-scalar-evolution.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-address.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-alias.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-ccp.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-coalesce.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-dce.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-dom.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-live.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-loop-ivopts.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-loop-manip.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-loop-niter.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-loop.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-operands.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-propagate.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-sccvn.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-scopedtables.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-strlen.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-ter.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-threadedge.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa-threadupdate.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssa.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-ssanames.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-stdarg.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-streamer.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-vector-builder.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-vectorizer.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree-vrp.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tree.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tsan.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/tsystem.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/typeclass.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/typed-splay-tree.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/ubsan.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/valtrack.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/value-prof.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/varasm.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/vec-perm-indices.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/vec.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/vector-builder.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/version.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/vmsdbg.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/vr-values.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/vtable-verify.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/wide-int-bitmask.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/wide-int-print.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/wide-int.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/xcoff.h
/usr/share/xtensa-apl-elf/lib/gcc/xtensa-apl-elf/8.1.0/plugin/include/xcoffout.h
