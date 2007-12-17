Name: showfont
Version: 1.0.1
Release: %mkrel 3
Summary: Font dumper for X font server
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libfs-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Showfont  displays  data  about  a font that matches the given pattern.
The information shown includes font information, font properties, character
metrics, and character bitmaps.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/showfont
%{_mandir}/man1/showfont.*


