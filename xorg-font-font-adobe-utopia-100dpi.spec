# $Rev: 3192 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	font-adobe-utopia-100dpi
Summary(pl):	font-adobe-utopia-100dpi
Name:		xorg-font-font-adobe-utopia-100dpi
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-adobe-utopia-100dpi-%{version}.tar.bz2
# Source0-md5:	71ef49367ab5a43209ecfd931aaf5d72
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/font-adobe-utopia-100dpi-%{version}-root-%(id -u -n)

%description
font-adobe-utopia-100dpi

%description -l pl
font-adobe-utopia-100dpi


%prep
%setup -q -n font-adobe-utopia-100dpi-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/100dpi/*
