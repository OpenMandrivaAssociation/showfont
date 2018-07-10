Name: showfont
Version: 1.0.5
Release: 3
Summary: Font dumper for X font server
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRequires: libfs-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

Patch1: 0001-Update-to-match-mandriva-default-fontserver-config.patch

%description
Showfont  displays  data  about  a font that matches the given pattern.
The information shown includes font information, font properties, character
metrics, and character bitmaps.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1

%build
%configure	\
		--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/showfont
%{_mandir}/man1/showfont.*
