Summary:	Font dumper for X font server
Name:		showfont
Version:	1.0.6
Release:	2
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
Patch1:		0001-Update-to-match-mandriva-default-fontserver-config.patch
BuildRequires:	pkgconfig(libfs)
BuildRequires:	pkgconfig(xorg-macros)

%description
Showfont  displays  data  about  a font that matches the given pattern.
The information shown includes font information, font properties, character
metrics, and character bitmaps.

%prep
%autosetup -p1

%build
%configure \
    --x-includes=%{_includedir} \
    --x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/showfont
%doc %{_mandir}/man1/showfont.*
