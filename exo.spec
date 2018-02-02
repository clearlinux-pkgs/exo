#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : exo
Version  : 0.11.5
Release  : 18
URL      : http://archive.xfce.org/src/xfce/exo/0.11/exo-0.11.5.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/exo/0.11/exo-0.11.5.tar.bz2
Summary  : Extension library for Xfce
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: exo-bin
Requires: exo-lib
Requires: exo-data
Requires: exo-doc
Requires: exo-locales
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl-URI
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(x11)

%description
What is it?
===========
This is libexo, an extension library to Xfce, originally developed by
os-cillation. While Xfce comes with quite a few libraries that are targeted at
desktop development, libexo is targeted at application development.

%package bin
Summary: bin components for the exo package.
Group: Binaries
Requires: exo-data

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
Requires: exo-lib
Requires: exo-bin
Requires: exo-data
Provides: exo-devel

%description dev
dev components for the exo package.


%package doc
Summary: doc components for the exo package.
Group: Documentation

%description doc
doc components for the exo package.


%package lib
Summary: lib components for the exo package.
Group: Libraries
Requires: exo-data

%description lib
lib components for the exo package.


%package locales
Summary: locales components for the exo package.
Group: Default

%description locales
locales components for the exo package.


%prep
%setup -q -n exo-0.11.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503069588
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1503069588
rm -rf %{buildroot}
%make_install
%find_lang exo-1
## make_install_append content
mv %{buildroot}%{_sysconfdir}/xdg %{buildroot}%{_datadir}/. && rmdir %{buildroot}%{_sysconfdir}
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/xfce4/exo-1/exo-compose-mail-1
/usr/lib64/xfce4/exo-1/exo-helper-1

%files bin
%defattr(-,root,root,-)
/usr/bin/exo-csource
/usr/bin/exo-desktop-item-edit
/usr/bin/exo-open
/usr/bin/exo-preferred-applications

%files data
%defattr(-,root,root,-)
/usr/share/applications/exo-file-manager.desktop
/usr/share/applications/exo-mail-reader.desktop
/usr/share/applications/exo-preferred-applications.desktop
/usr/share/applications/exo-terminal-emulator.desktop
/usr/share/applications/exo-web-browser.desktop
/usr/share/icons/hicolor/24x24/apps/preferences-desktop-default-applications.png
/usr/share/icons/hicolor/48x48/apps/preferences-desktop-default-applications.png
/usr/share/pixmaps/exo-1/exo-thumbnail-frame.png
/usr/share/xdg/xfce4/helpers.rc
/usr/share/xfce4/helpers/Thunar.desktop
/usr/share/xfce4/helpers/aterm.desktop
/usr/share/xfce4/helpers/balsa.desktop
/usr/share/xfce4/helpers/brave.desktop
/usr/share/xfce4/helpers/caja.desktop
/usr/share/xfce4/helpers/chromium.desktop
/usr/share/xfce4/helpers/debian-sensible-browser.desktop
/usr/share/xfce4/helpers/debian-x-terminal-emulator.desktop
/usr/share/xfce4/helpers/dillo.desktop
/usr/share/xfce4/helpers/encompass.desktop
/usr/share/xfce4/helpers/epiphany.desktop
/usr/share/xfce4/helpers/eterm.desktop
/usr/share/xfce4/helpers/evolution.desktop
/usr/share/xfce4/helpers/firefox.desktop
/usr/share/xfce4/helpers/galeon.desktop
/usr/share/xfce4/helpers/geary.desktop
/usr/share/xfce4/helpers/gnome-terminal.desktop
/usr/share/xfce4/helpers/google-chrome.desktop
/usr/share/xfce4/helpers/icecat.desktop
/usr/share/xfce4/helpers/icedove.desktop
/usr/share/xfce4/helpers/iceweasel.desktop
/usr/share/xfce4/helpers/jumanji.desktop
/usr/share/xfce4/helpers/kmail.desktop
/usr/share/xfce4/helpers/konqueror.desktop
/usr/share/xfce4/helpers/links.desktop
/usr/share/xfce4/helpers/lynx.desktop
/usr/share/xfce4/helpers/midori.desktop
/usr/share/xfce4/helpers/mozilla-browser.desktop
/usr/share/xfce4/helpers/mozilla-mailer.desktop
/usr/share/xfce4/helpers/mutt.desktop
/usr/share/xfce4/helpers/nautilus.desktop
/usr/share/xfce4/helpers/netscape-navigator.desktop
/usr/share/xfce4/helpers/nxterm.desktop
/usr/share/xfce4/helpers/opera-browser.desktop
/usr/share/xfce4/helpers/pcmanfm.desktop
/usr/share/xfce4/helpers/qterminal.desktop
/usr/share/xfce4/helpers/qtfm.desktop
/usr/share/xfce4/helpers/qupzilla.desktop
/usr/share/xfce4/helpers/rodent.desktop
/usr/share/xfce4/helpers/rox-filer.desktop
/usr/share/xfce4/helpers/sakura.desktop
/usr/share/xfce4/helpers/surf.desktop
/usr/share/xfce4/helpers/sylpheed-claws.desktop
/usr/share/xfce4/helpers/sylpheed.desktop
/usr/share/xfce4/helpers/terminator.desktop
/usr/share/xfce4/helpers/thunderbird.desktop
/usr/share/xfce4/helpers/urxvt.desktop
/usr/share/xfce4/helpers/vimprobable2.desktop
/usr/share/xfce4/helpers/w3m.desktop
/usr/share/xfce4/helpers/xfce4-terminal.desktop
/usr/share/xfce4/helpers/xfe.desktop
/usr/share/xfce4/helpers/xterm.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/exo-1/exo/exo-binding.h
/usr/include/exo-1/exo/exo-cell-renderer-ellipsized-text.h
/usr/include/exo-1/exo/exo-cell-renderer-icon.h
/usr/include/exo-1/exo/exo-config.h
/usr/include/exo-1/exo/exo-enum-types.h
/usr/include/exo-1/exo/exo-execute.h
/usr/include/exo-1/exo/exo-gdk-pixbuf-extensions.h
/usr/include/exo-1/exo/exo-gobject-extensions.h
/usr/include/exo-1/exo/exo-gtk-extensions.h
/usr/include/exo-1/exo/exo-icon-bar.h
/usr/include/exo-1/exo/exo-icon-chooser-dialog.h
/usr/include/exo-1/exo/exo-icon-view.h
/usr/include/exo-1/exo/exo-job.h
/usr/include/exo-1/exo/exo-simple-job.h
/usr/include/exo-1/exo/exo-string.h
/usr/include/exo-1/exo/exo-toolbars-editor-dialog.h
/usr/include/exo-1/exo/exo-toolbars-editor.h
/usr/include/exo-1/exo/exo-toolbars-model.h
/usr/include/exo-1/exo/exo-toolbars-view.h
/usr/include/exo-1/exo/exo-tree-view.h
/usr/include/exo-1/exo/exo-utils.h
/usr/include/exo-1/exo/exo-wrap-table.h
/usr/include/exo-1/exo/exo-xsession-client.h
/usr/include/exo-1/exo/exo.h
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
/usr/include/exo-2/exo/exo-toolbars-model.h
/usr/include/exo-2/exo/exo-tree-view.h
/usr/include/exo-2/exo/exo-utils.h
/usr/include/exo-2/exo/exo.h
/usr/lib64/libexo-1.so
/usr/lib64/libexo-2.so
/usr/lib64/pkgconfig/exo-1.pc
/usr/lib64/pkgconfig/exo-2.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/gtk-doc/html/exo-1/ExoCellRendererEllipsizedText.html
/usr/share/gtk-doc/html/exo-1/ExoCellRendererIcon.html
/usr/share/gtk-doc/html/exo-1/ExoIconBar.html
/usr/share/gtk-doc/html/exo-1/ExoIconChooserDialog.html
/usr/share/gtk-doc/html/exo-1/ExoIconView.html
/usr/share/gtk-doc/html/exo-1/ExoJob.html
/usr/share/gtk-doc/html/exo-1/ExoSimpleJob.html
/usr/share/gtk-doc/html/exo-1/ExoToolbarsEditor.html
/usr/share/gtk-doc/html/exo-1/ExoToolbarsEditorDialog.html
/usr/share/gtk-doc/html/exo-1/ExoToolbarsModel.html
/usr/share/gtk-doc/html/exo-1/ExoToolbarsView.html
/usr/share/gtk-doc/html/exo-1/ExoTreeView.html
/usr/share/gtk-doc/html/exo-1/ExoWrapTable.html
/usr/share/gtk-doc/html/exo-1/ExoXsessionClient.html
/usr/share/gtk-doc/html/exo-1/ch01.html
/usr/share/gtk-doc/html/exo-1/ch02.html
/usr/share/gtk-doc/html/exo-1/exo-1.devhelp2
/usr/share/gtk-doc/html/exo-1/exo-Binding-Properties-Functions.html
/usr/share/gtk-doc/html/exo-1/exo-Executing-Applications.html
/usr/share/gtk-doc/html/exo-1/exo-Extensions-to-GObject.html
/usr/share/gtk-doc/html/exo-1/exo-Extensions-to-Gtk.html
/usr/share/gtk-doc/html/exo-1/exo-Extensions-to-gdk-pixbuf.html
/usr/share/gtk-doc/html/exo-1/exo-Miscellaneous-Utility-Functions.html
/usr/share/gtk-doc/html/exo-1/exo-String-Utility-Functions.html
/usr/share/gtk-doc/html/exo-1/exo-Version-Information.html
/usr/share/gtk-doc/html/exo-1/exo-cell-renderers.html
/usr/share/gtk-doc/html/exo-1/exo-csource.html
/usr/share/gtk-doc/html/exo-1/exo-extensions.html
/usr/share/gtk-doc/html/exo-1/exo-gtk-file-chooser-add-thumbnail-preview.png
/usr/share/gtk-doc/html/exo-1/exo-icon-chooser-dialog.png
/usr/share/gtk-doc/html/exo-1/exo-jobs.html
/usr/share/gtk-doc/html/exo-1/exo-miscelleanous.html
/usr/share/gtk-doc/html/exo-1/exo-overview.html
/usr/share/gtk-doc/html/exo-1/exo-toolbars-editor-dialog.png
/usr/share/gtk-doc/html/exo-1/exo-toolbars-editor.png
/usr/share/gtk-doc/html/exo-1/exo-toolbars-view.png
/usr/share/gtk-doc/html/exo-1/exo-toolbars.html
/usr/share/gtk-doc/html/exo-1/exo-tools.html
/usr/share/gtk-doc/html/exo-1/exo-widgets.html
/usr/share/gtk-doc/html/exo-1/exo-wrap-table.png
/usr/share/gtk-doc/html/exo-1/home.png
/usr/share/gtk-doc/html/exo-1/index.html
/usr/share/gtk-doc/html/exo-1/ix14.html
/usr/share/gtk-doc/html/exo-1/left-insensitive.png
/usr/share/gtk-doc/html/exo-1/left.png
/usr/share/gtk-doc/html/exo-1/right-insensitive.png
/usr/share/gtk-doc/html/exo-1/right.png
/usr/share/gtk-doc/html/exo-1/style.css
/usr/share/gtk-doc/html/exo-1/up-insensitive.png
/usr/share/gtk-doc/html/exo-1/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libexo-1.so.0
/usr/lib64/libexo-1.so.0.1.0
/usr/lib64/libexo-2.so.0
/usr/lib64/libexo-2.so.0.1.0

%files locales -f exo-1.lang
%defattr(-,root,root,-)
