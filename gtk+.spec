%define major    1.2
%define libname  %mklibname gtk+ %{major}

Summary:	The GIMP ToolKit (GTK+), a library for creating GUIs for X
Name:		gtk+
Version:	1.2.10
Release:	%mkrel 45
License:	LGPL
Group:		System/Libraries
Source0:	ftp://ftp.gimp.org/pub/gtk/v1.2/gtk+-%{version}.tar.bz2
Source1:	gtk+-1.2.10-vi.po.bz2	
# (fc) 1.2.10-2mdk ximian patch changing drawing when no shadow is set for menubar
Patch2:		gtkmenubar-noborder.patch.bz2
# (pablo) better gtkrc definitions
Patch3:		gtk+-1.2.10-gtkrc_files.patch.bz2
# (fc) 1.2.10-8mdk GNOME CVS patch correcting bad focus (seen in Evolution and gnomecc)
Patch4:		gtk+-1.2.10-focus.patch.bz2
# (pablo) load locale based gtkrc (GNOME CVS)
Patch5:		gtk+-1.2.10-rclocale.patch.bz2
# (fc) 1.2.10-10mdk fix alignement warning on ia64 (Rawhide)
Patch6:		gtk+-1.2.10-alignment.patch.bz2
# (fc) 1.2.10-10mdk Improve exposure compression (GNOME CVS)
Patch7:		gtk+-1.2.10-expose.patch.bz2
# (fc) 1.2.10-10mdk Don't screw up CTEXT encoding for UTF-8 (Rawhide)
Patch8:		gtk+-1.2.10-ctext.patch.bz2
# (fc) 1.2.10-10mdk Accept KP_Enter as a synonym for Return everywhere (Rawhide)
Patch9:		gtk+-1.2.10-kpenter.patch.bz2
# (fc) 1.2.10-10mdk Allow theme switching to work properly when no windows are realized (Rawhide)
Patch10:	gtk+-1.2.10-themeswitch.patch.bz2
# (fc) 1.2.10-10mdk Fix crash when switching themes (Rawhide)
Patch11:	gtk+-1.2.10-pixmapref.patch.bz2
# (fc) 1.2.10-10mdk Fix computation of width of missing characters (Rawhide)
Patch12:	gtk+-1.2.10-missingchar.patch.bz2
# (fc) 1.2.10-20mdk set _NET_WM_PID on gdkwindow (GNOME CVS)
Patch15:	gtk+-1.2.10-netwmpid.patch.bz2
# (fc) 1.2.10-22mdk fix Fix check of wrong variable on gtklabel (GNOME CVS)
Patch16:	gtk+-1.2.10-labelvariable.patch.bz2
# (fc) 1.2.10-22mdk fix GtkCombo occasionally segfaults after content is changed and list shown (GNOME CVS) Bugzilla 58024
Patch17:	gtk+-1.2.10-gtklist.patch.bz2
# (fc) 1.2.10-22mdk option menu doesn't appear centered when applied a border (GNOME CVS) Bugzilla 54585
Patch18:	gtk+-1.2.10-border.patch.bz2
# (fc) 1.2.10-22mdk DnD code doesn't notice new windows (GNOME CVS) Bugzilla 56349
Patch19:	gtk+-1.2.10-dndnewwindow.patch.bz2
# (fc) 1.2.10-26mdk don't set -L/usr/lib in gtk-config
Patch20:	gtk+-1.2.10-libdir.patch.bz2
# (fc) 1.2.10-27mdk Fix file selection delete-dir when changing directory problem
# also, fix memory corruption problem when changing directories. (Rawhide)
Patch21:	gtk+-1.2.10-deletedir.patch.bz2 
# fc) 1.2.10-27mdk Improve warning for missing fonts (Rawhide)
Patch22:	gtk+-1.2.10-fontwarning.patch.bz2
# (fc) 1.2.10-27mdk Allow themes to make scrollbar trough always repaint (rawhide)
Patch23:	gtk+-1.2.10-troughpaint.patch.bz2
# (fc) 1.2.10-28mdk Fix a crash that can happen in some apps when the current
# locale is not supported by XLib. (rawhide)
Patch24:	gtk+-1.2.10-localecrash.patch.bz2
# (fc) 1.2.10-29mdk fix loop and crash in file selector when / is not readable (bug #90)
Patch25:	gtk+-1.2.10-fileselectorfallback.patch.bz2
# (fc) 1.2.10-30mdk change default colors to match GTK2 2.2 colors
Patch26:	gtk+-1.2.10-defaultcolor.patch.bz2
Patch27:	gtk+-1.2.10-fix-underquoted-calls.patch.bz2
# (fc) 1.2.10-45mdv ugly hack to skip argb visuals
Patch28:	gtk+-1.2.10-argb.patch.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.gtk.org
BuildRequires:	XFree86-devel
BuildRequires:	autoconf2.1
BuildRequires:	libtool
BuildRequires:	glib-devel >= %{version}

%description
The gtk+ package contains the GIMP ToolKit (GTK+), a library for creating
graphical user interfaces for the X Window System.  GTK+ was originally
written for the GIMP (GNU Image Manipulation Program) image processing
program, but is now used by several other programs as well.  

If you are planning on using the GIMP or another program that uses GTK+,
you'll need to have the gtk+ package installed.

%package -n	%{libname}
Summary:	Main library for gtk+
Group:		System/Libraries
Provides:	gtk+ = %{version}-%{release}
Obsoletes:	gtk+

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with gtk+.

%package -n	%{libname}-devel
Summary:	Development tools for GTK+ (GIMP ToolKit) applications
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Obsoletes:	gtk-devel
Requires(post,preun):	/sbin/install-info
Provides:	gtk-devel = %{version}-%{release}
Provides:	gtk+-devel = %{version}-%{release}
Provides:	libgtk+-devel = %{version}-%{release}
Provides:	gtk+%{major}-devel = %{version}-%{release}
Obsoletes:	gtk+-devel

%description -n	%{libname}-devel
The libgtk+1.2-devel package contains the static libraries and header files
needed for developing GTK+ (GIMP ToolKit) applications. The libgtk+1.2-devel
package contains GDK (the General Drawing Kit, which simplifies the interface
for writing GTK+ widgets and using GTK+ widgets in applications), and GTK+
(the widget set).

Install libgtk+1.2-devel if you need to develop GTK+ applications.  You'll also
need to install the gtk+ package.

%prep
%setup -q
%patch2 -p1 -b .noshadow
%patch3 -p1 -b .gtkrc
%patch4 -p1 -b .focus
%patch5 -p1 -b .rclocale
%patch6 -p1 -b .ia64
%patch7 -p1 -b .expose
%patch8 -p1 -b .ctext
%patch9 -p1 -b .kpenter
%patch10 -p1 -b .themeswitch
%patch11 -p1 -b .pixmapref
%patch12 -p1 -b .missingchar
%patch15 -p1 -b .netwmpid
%patch16 -p1 -b .labelvariable
%patch17 -p1 -b .gtklist
%patch18 -p1 -b .border
%patch19 -p1 -b .dndnewwindow
%patch20 -p1 -b .libdir
%patch21 -p1 -b .deletedir
%patch22 -p1 -b .fontwarning
%patch23 -p1 -b .troughpaint
%patch24 -p1 -b .localecrash
%patch25 -p1 -b .fileselectorfallback
%patch26 -p1 -b .defaultcolor
%patch27 -p1 -b .underquoted
%patch28 -p1 -b .argb

# vi.po is not encoded in utf-8
bzcat %{SOURCE1} > po/vi.po

# needed by patch 3
autoheader
autoconf

%build
%configure  --with-xinput=xfree --with-native-locale
%make LIBTOOL=%{_bindir}/libtool

make check

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/*

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%post -n %{libname}-devel
%_install_info gtk.info
%_install_info gdk.info

%preun -n %{libname}-devel
if [ "$1" = "0" ]; then
	%{__install_info} \
	%{_infodir}/gdk.info%{_extension} --dir=%{_infodir}/dir --remove
fi
if [ "$1" = "0" ]; then
	%{__install_info} \
	%{_infodir}/gtk.info%{_extension} --dir=%{_infodir}/dir --remove
fi

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname} -f %{name}.lang
%defattr(-, root, root)
%doc INSTALL ABOUT-NLS
%{_libdir}/lib*.so.*
%{_datadir}/themes
%dir %{_sysconfdir}/gtk
%config(noreplace) %{_sysconfdir}/gtk/*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc docs/*.txt AUTHORS ChangeLog NEWS* README* TODO docs/html
%{_libdir}/lib*.so
%{_libdir}/*a
%{_mandir}/man1/*
%{_infodir}/g?k.info*
%{_includedir}/*
%{_datadir}/aclocal/*
%multiarch %{multiarch_bindir}/*
%{_bindir}/*
%{_libdir}/pkgconfig/*
