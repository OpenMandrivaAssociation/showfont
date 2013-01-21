Name: showfont
Version: 1.0.4
Release: 1
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
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/showfont
%{_mandir}/man1/showfont.*




%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 669979
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 592507
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdv2010.1
+ Revision: 524075
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-3mdv2010.0
+ Revision: 427139
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2009.0
+ Revision: 265695
- rebuild early 2009.0 package (before pixel changes)

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 1.0.2-1mdv2009.0
+ Revision: 211826
- New version

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 166441
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Wed Jan 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-4mdv2008.1
+ Revision: 153857
- Use git-archive to generate tarball.
  Add patch to changed default -server option to Mandriva standard xfs.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2008.0
+ Revision: 67260
- fix man pages extension


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Wed May 17 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-17 00:18:30 (27489)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

