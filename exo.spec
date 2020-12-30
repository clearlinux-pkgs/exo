#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : exo
Version  : 4.16.0
Release  : 33
URL      : https://archive.xfce.org/xfce/4.16/src/exo-4.16.0.tar.bz2
Source0  : https://archive.xfce.org/xfce/4.16/src/exo-4.16.0.tar.bz2
Summary  : Extension library for Xfce
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: exo-bin = %{version}-%{release}
Requires: exo-data = %{version}-%{release}
Requires: exo-lib = %{version}-%{release}
Requires: exo-license = %{version}-%{release}
Requires: exo-locales = %{version}-%{release}
Requires: exo-man = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl
BuildRequires : perl-URI
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)

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
%setup -q -n exo-4.16.0
cd %{_builddir}/exo-4.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609286641
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1609286641
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/exo
cp %{_builddir}/exo-4.16.0/COPYING %{buildroot}/usr/share/package-licenses/exo/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/exo-4.16.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/exo/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install
%find_lang exo-2
## install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/. && rmdir %{buildroot}%{_sysconfdir}

## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/exo-desktop-item-edit
/usr/bin/exo-open

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/24x24/apps/preferences-desktop-default-applications.png
/usr/share/icons/hicolor/48x48/apps/preferences-desktop-default-applications.png
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
/usr/share/gtk-doc/html/exo-2/ch02.html
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
/usr/share/gtk-doc/html/exo-2/exo-gtk-file-chooser-add-thumbnail-preview.png
/usr/share/gtk-doc/html/exo-2/exo-icon-chooser-dialog.png
/usr/share/gtk-doc/html/exo-2/exo-jobs.html
/usr/share/gtk-doc/html/exo-2/exo-miscelleanous.html
/usr/share/gtk-doc/html/exo-2/exo-overview.html
/usr/share/gtk-doc/html/exo-2/exo-widgets.html
/usr/share/gtk-doc/html/exo-2/home.png
/usr/share/gtk-doc/html/exo-2/index.html
/usr/share/gtk-doc/html/exo-2/ix14.html
/usr/share/gtk-doc/html/exo-2/left-insensitive.png
/usr/share/gtk-doc/html/exo-2/left.png
/usr/share/gtk-doc/html/exo-2/right-insensitive.png
/usr/share/gtk-doc/html/exo-2/right.png
/usr/share/gtk-doc/html/exo-2/style.css
/usr/share/gtk-doc/html/exo-2/up-insensitive.png
/usr/share/gtk-doc/html/exo-2/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libexo-2.so.0
/usr/lib64/libexo-2.so.0.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/exo/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/exo/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/exo-open.1

%files locales -f exo-2.lang
%defattr(-,root,root,-)

