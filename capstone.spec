#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : capstone
Version  : 5.0.1
Release  : 4
URL      : https://github.com/aquynh/capstone/archive/5.0.1/capstone-5.0.1.tar.gz
Source0  : https://github.com/aquynh/capstone/archive/5.0.1/capstone-5.0.1.tar.gz
Summary  : A lightweight multi-platform, multi-architecture disassembly framework
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause NCSA
Requires: capstone-bin = %{version}-%{release}
Requires: capstone-lib = %{version}-%{release}
Requires: capstone-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(cmocka)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Capstone is a disassembly framework with the target of becoming the ultimate
disasm engine for binary analysis and reversing in the security community.

%package bin
Summary: bin components for the capstone package.
Group: Binaries
Requires: capstone-license = %{version}-%{release}

%description bin
bin components for the capstone package.


%package dev
Summary: dev components for the capstone package.
Group: Development
Requires: capstone-lib = %{version}-%{release}
Requires: capstone-bin = %{version}-%{release}
Provides: capstone-devel = %{version}-%{release}
Requires: capstone = %{version}-%{release}

%description dev
dev components for the capstone package.


%package lib
Summary: lib components for the capstone package.
Group: Libraries
Requires: capstone-license = %{version}-%{release}

%description lib
lib components for the capstone package.


%package license
Summary: license components for the capstone package.
Group: Default

%description license
license components for the capstone package.


%prep
%setup -q -n capstone-5.0.1
cd %{_builddir}/capstone-5.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692730560
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../clr-build-avx2;
make test || :

%install
export SOURCE_DATE_EPOCH=1692730560
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/capstone
cp %{_builddir}/capstone-%{version}/LICENSE.TXT %{buildroot}/usr/share/package-licenses/capstone/861af24907e399e873920dbbff1ea1dd73a9ba35 || :
cp %{_builddir}/capstone-%{version}/LICENSE_LLVM.TXT %{buildroot}/usr/share/package-licenses/capstone/afc034c0ae47cbd47a99c6c5992d846511bb33ad || :
cp %{_builddir}/capstone-%{version}/bindings/python/LICENSE.TXT %{buildroot}/usr/share/package-licenses/capstone/861af24907e399e873920dbbff1ea1dd73a9ba35 || :
cp %{_builddir}/capstone-%{version}/bindings/vb6/Apache_2.0_License.txt %{buildroot}/usr/share/package-licenses/capstone/47b573e3824cd5e02a1a3ae99e2735b49e0256e4 || :
cp %{_builddir}/capstone-%{version}/suite/regress/LICENSE %{buildroot}/usr/share/package-licenses/capstone/7de9d56eea42f5bbbba6fff880d912f2c9c3a45d || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/cstool
/usr/bin/cstool

%files dev
%defattr(-,root,root,-)
/usr/include/capstone/arm.h
/usr/include/capstone/arm64.h
/usr/include/capstone/bpf.h
/usr/include/capstone/capstone.h
/usr/include/capstone/evm.h
/usr/include/capstone/m680x.h
/usr/include/capstone/m68k.h
/usr/include/capstone/mips.h
/usr/include/capstone/mos65xx.h
/usr/include/capstone/platform.h
/usr/include/capstone/ppc.h
/usr/include/capstone/riscv.h
/usr/include/capstone/sh.h
/usr/include/capstone/sparc.h
/usr/include/capstone/systemz.h
/usr/include/capstone/tms320c64x.h
/usr/include/capstone/tricore.h
/usr/include/capstone/wasm.h
/usr/include/capstone/x86.h
/usr/include/capstone/xcore.h
/usr/lib64/cmake/capstone/capstone-config-version.cmake
/usr/lib64/cmake/capstone/capstone-config.cmake
/usr/lib64/cmake/capstone/capstone-targets-relwithdebinfo.cmake
/usr/lib64/cmake/capstone/capstone-targets.cmake
/usr/lib64/libcapstone.so
/usr/lib64/pkgconfig/capstone.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libcapstone.so.5.0
/usr/lib64/libcapstone.so.5
/usr/lib64/libcapstone.so.5.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/capstone/47b573e3824cd5e02a1a3ae99e2735b49e0256e4
/usr/share/package-licenses/capstone/7de9d56eea42f5bbbba6fff880d912f2c9c3a45d
/usr/share/package-licenses/capstone/861af24907e399e873920dbbff1ea1dd73a9ba35
/usr/share/package-licenses/capstone/afc034c0ae47cbd47a99c6c5992d846511bb33ad
