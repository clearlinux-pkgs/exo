#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: 5424026
#
Name     : exo
Version  : 4.20.0
Release  : 39
URL      : https://archive.xfce.org/src/xfce/exo/4.20/exo-4.20.0.tar.bz2
Source0  : https://archive.xfce.org/src/xfce/exo/4.20/exo-4.20.0.tar.bz2
Summary  : Extension library for Xfce
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: exo-bin = %{version}-%{release}
Requires: exo-data = %{version}-%{release}
Requires: exo-lib = %{version}-%{release}
Requires: exo-license = %{version}-%{release}
Requires: exo-locales = %{version}-%{release}
Requires: exo-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : file
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : perl-URI
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.xfce.org/xfce/exo/COPYING)

%package bin
Summary: bin components for the exo package.
Group: Binaries
Requires: exo-data = %{version}-%{release}
Requires: exo-license = %{version}-%{release}

%description bin
bin components for the exo package.


%package data
Summary: data components for the exo package.
Group: Data

%description data
data components for the exo package.


%package dev
Summary: dev components for the exo package.
Group: Development
Requires: exo-lib = %{version}-%{release}
Requires: exo-bin = %{version}-%{release}
Requires: exo-data = %{version}-%{release}
Provides: exo-devel = %{version}-%{release}
Requires: exo = %{version}-%{release}

%description dev
dev components for the exo package.


%package doc
Summary: doc components for the exo package.
Group: Documentation
Requires: exo-man = %{version}-%{release}

%description doc
doc components for the exo package.


%package lib
Summary: lib components for the exo package.
Group: Libraries
Requires: exo-data = %{version}-%{release}
Requires: exo-license = %{version}-%{release}

%description lib
lib components for the exo package.


%package license
Summary: license components for the exo package.
Group: Default

%description license
license components for the exo package.


%package locales
Summary: locales components for the exo package.
Group: Default

%description locales
locales components for the exo package.


%package man
Summary: man components for the exo package.
Group: Default

%description man
man components for the exo package.


%prep
%setup -q -n exo-4.20.0
cd %{_builddir}/exo-4.20.0
pushd ..
cp -a exo-4.20.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735079263
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735079263
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/exo
cp %{_builddir}/exo-%{version}/COPYING %{buildroot}/usr/share/package-licenses/exo/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/exo-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/exo/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang exo
## install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/. && rmdir %{buildroot}%{_sysconfdir}

## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/exo-desktop-item-edit
/V3/usr/bin/exo-open
/usr/bin/exo-desktop-item-edit
/usr/bin/exo-open

%files data
%defattr(-,root,root,-)
/usr/share/pixmaps/exo/exo-thumbnail-frame.png

%files dev
%defattr(-,root,root,-)
/usr/include/exo-2/exo/exo-binding.h
/usr/include/exo-2/exo/exo-cell-renderer-icon.h
/usr/include/exo-2/exo/exo-config.h
/usr/include/exo-2/exo/exo-enum-types.h
/usr/include/exo-2/exo/exo-execute.h
/usr/include/exo-2/exo/exo-gdk-pixbuf-extensions.h
/usr/include/exo-2/exo/exo-gobject-extensions.h
/usr/include/exo-2/exo/exo-gtk-extensions.h
/usr/include/exo-2/exo/exo-icon-chooser-dialog.h
/usr/include/exo-2/exo/exo-icon-chooser-model.h
/usr/include/exo-2/exo/exo-icon-view.h
/usr/include/exo-2/exo/exo-job.h
/usr/include/exo-2/exo/exo-simple-job.h
/usr/include/exo-2/exo/exo-string.h
/usr/include/exo-2/exo/exo-thumbnail-preview.h
/usr/include/exo-2/exo/exo-thumbnail.h
/usr/include/exo-2/exo/exo-tree-view.h
/usr/include/exo-2/exo/exo-utils.h
/usr/include/exo-2/exo/exo.h
/usr/lib64/libexo-2.so
/usr/lib64/pkgconfig/exo-2.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/exo-2/ExoCellRendererIcon.html
/usr/share/gtk-doc/html/exo-2/ExoIconChooserDialog.html
/usr/share/gtk-doc/html/exo-2/ExoIconView.html
/usr/share/gtk-doc/html/exo-2/ExoJob.html
/usr/share/gtk-doc/html/exo-2/ExoSimpleJob.html
/usr/share/gtk-doc/html/exo-2/ExoTreeView.html
/usr/share/gtk-doc/html/exo-2/ch01.html
/usr/share/gtk-doc/html/exo-2/exo-2.devhelp2
/usr/share/gtk-doc/html/exo-2/exo-Binding-Properties-Functions.html
/usr/share/gtk-doc/html/exo-2/exo-Executing-Applications.html
/usr/share/gtk-doc/html/exo-2/exo-Extensions-to-GObject.html
/usr/share/gtk-doc/html/exo-2/exo-Extensions-to-Gtk.html
/usr/share/gtk-doc/html/exo-2/exo-Extensions-to-gdk-pixbuf.html
/usr/share/gtk-doc/html/exo-2/exo-Miscellaneous-Utility-Functions.html
/usr/share/gtk-doc/html/exo-2/exo-String-Utility-Functions.html
/usr/share/gtk-doc/html/exo-2/exo-Version-Information.html
/usr/share/gtk-doc/html/exo-2/exo-cell-renderers.html
/usr/share/gtk-doc/html/exo-2/exo-extensions.html
/usr/share/gtk-doc/html/exo-2/exo-jobs.html
/usr/share/gtk-doc/html/exo-2/exo-miscelleanous.html
/usr/share/gtk-doc/html/exo-2/exo-overview.html
/usr/share/gtk-doc/html/exo-2/exo-widgets.html
/usr/share/gtk-doc/html/exo-2/home.png
/usr/share/gtk-doc/html/exo-2/index.html
/usr/share/gtk-doc/html/exo-2/ix15.html
/usr/share/gtk-doc/html/exo-2/left-insensitive.png
/usr/share/gtk-doc/html/exo-2/left.png
/usr/share/gtk-doc/html/exo-2/right-insensitive.png
/usr/share/gtk-doc/html/exo-2/right.png
/usr/share/gtk-doc/html/exo-2/style.css
/usr/share/gtk-doc/html/exo-2/up-insensitive.png
/usr/share/gtk-doc/html/exo-2/up.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libexo-2.so.0.1.0
/usr/lib64/libexo-2.so.0
/usr/lib64/libexo-2.so.0.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/exo/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/exo/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/exo-open.1

%files locales -f exo.lang
%defattr(-,root,root,-)

