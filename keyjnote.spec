%define tarname KeyJnote
%define name keyjnote
%define version 0.10.2
%define release 5

Summary: OpenGL-based slide presentation program
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{tarname}-%{version}.tar.gz
License: GPLv2
Group: Office
Url: http://keyjnote.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: python >= 2.3
Requires: python-opengl, pygame, python-imaging
Suggests: xpdf, ghostscript, pdftk, xdg-utils, mplayer

%description
KeyJnote is a simple presentation program that displays slideshows of image
files (JPEG, PNG, TIFF, and BMP) or PDF documents. Rendering is done via
OpenGL, which allows for some "eye candy" effects.

%prep
%setup -q -n %{tarname}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__install -D -m 755 keyjnote.py %{buildroot}%{_bindir}/keyjnote

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc keyjnote.html demo.pdf license.txt
%{_bindir}/%{name}*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.2-4mdv2011.0
+ Revision: 619962
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.10.2-3mdv2010.0
+ Revision: 429669
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.10.2-2mdv2009.0
+ Revision: 267784
- rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Lev Givon <lev@mandriva.org> 0.10.2-1mdv2009.0
+ Revision: 218605
- import keyjnote


* Thu Jun 12 2008 Lev Givon <lev@mandriva.org> 0.10.2-1mdv2008.1
- Package for Mandrive.
