Summary:	Link-local XMPP connection manager for the Telepathy
Summary(pl.UTF-8):	Zarządca połączeń XMPP link-local dla Telepathy
Name:		telepathy-salut
Version:	0.8.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-salut/%{name}-%{version}.tar.gz
# Source0-md5:	7516e6f6fa56a61054413a03642b938d
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	avahi-glib-devel
BuildRequires:	avahi-gobject-devel
BuildRequires:	cyrus-sasl-devel >= 2
BuildRequires:	dbus-devel >= 1.1.0
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 1:2.28
BuildRequires:	gtk-doc >= 1.17
BuildRequires:	gtk-doc-automake >= 1.17
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	libxslt-progs
BuildRequires:	openssl-devel >= 0.9.8g
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	sqlite3-devel
BuildRequires:	telepathy-glib-devel >= 0.17.1
Requires:	dbus-glib >= 0.61
Requires:	dbus-libs >= 1.1.0
Requires:	glib2 >= 1:2.28
Requires:	openssl >= 0.9.8g
Requires:	telepathy-glib >= 0.17.1
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
%configure \
	--disable-avahi-tests \
	--disable-static \
	--with-tls=openssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# -j1 because of some race when installing libsalut-plugins.so and relinking its dependencies
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# private shared libraries, .la file/.so symlink not needed
%{__rm} $RPM_BUILD_ROOT%{_libdir}/telepathy/salut-0/lib/lib{salut-plugins,wocky}.{la,so}
# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/telepathy-salut/clique.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/clique.html
%attr(755,root,root) %{_libexecdir}/telepathy-salut
%dir %{_libdir}/telepathy/salut-0
%dir %{_libdir}/telepathy/salut-0/lib
%attr(755,root,root) %{_libdir}/telepathy/salut-0/lib/libsalut-plugins-%{version}.so
%attr(755,root,root) %{_libdir}/telepathy/salut-0/lib/libwocky-telepathy-salut-%{version}.so
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.salut.service
%{_datadir}/telepathy/managers/salut.manager
%{_mandir}/man8/telepathy-salut.8*
