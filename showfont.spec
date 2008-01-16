Name: showfont
Version: 1.0.1
Release: %mkrel 4
Summary: Font dumper for X font server
Group: Development/X11
URL: http://xorg.freedesktop.org

# Note local showfont-1.0.1@mandriva suggested on upstream
# Tag at git checkout 297c3b528742a1897a436d92a218dcf309466f07
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/app/showfont xorg/app/showfont
# cd xorg/app/showfont
# git-archive --format=tar --prefix=showfont-1.0.1/ showfont-1.0.1@mandriva | bzip2 -9 > showfont-1.0.1.tar.bz2
Source: %{name}-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch showfont-1.0.1@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-to-match-mandriva-default-fontserver-config.patch
########################################################################

BuildRequires: libfs-devel	>= 1.0.0
BuildRequires: x11-util-macros	>= 1.1.5

%description
Showfont  displays  data  about  a font that matches the given pattern.
The information shown includes font information, font properties, character
metrics, and character bitmaps.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir}\
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


