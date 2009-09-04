%define tarname KeyJnote
%define name keyjnote
%define version 0.10.2
%define release %mkrel 3

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

