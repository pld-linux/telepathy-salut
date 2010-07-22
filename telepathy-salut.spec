Summary:	Link-local XMPP connection manager for the Telepathy
Summary(pl.UTF-8):	Zarządca połączeń XMPP link-local dla Telepathy
Name:		telepathy-salut
Version:	0.3.12
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-salut/%{name}-%{version}.tar.gz
# Source0-md5:	95968f871737e7cd75e4df39b521b692
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	avahi-glib-devel
BuildRequires:	avahi-gobject-devel
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 2.4
BuildRequires:	gtk-doc-automake
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	telepathy-glib-devel >= 0.7.23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Link-local XMPP functionality for Telepathy.

%description -l pl.UTF-8
Ten pakiet udostępnia funkcjonalność XMPP link-local dla Telepathy.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/telepathy-salut
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.salut.service
%{_datadir}/telepathy/managers/salut.manager
%{_mandir}/man8/*
