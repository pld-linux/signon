#
# Conditional build:
%bcond_without	qt4	# qt4-based libsignon-qt binding

Summary:	Single Sign On libraries and daemon
Summary(pl.UTF-8):	Biblioteki i demon Single Sign On
Name:		signon
Version:	8.58
Release:	1
License:	LGPL v2.1
Group:		Libraries
#Source0Download: https://gitlab.com/accounts-sso/signond/tags?page=14
# TODO: in the future use fake GET arg to force sane filename on df
#Source0:	https://gitlab.com/accounts-sso/signond/repository/archive.tar.bz2?ref=VERSION_%{version}&fake_out=/%{name}-%{version}.tar.bz2
Source0:	archive.tar.gz%3Fref=VERSION_%{version}
# Source0-md5:	90c29b033fe78a124ecca044e28a789b
Patch0:		%{name}-cryptsetup.patch
URL:		https://gitlab.com/accounts-sso/signond
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtDBus-devel >= 4
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
%endif
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5DBus-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Network-devel >= 5
BuildRequires:	Qt5Sql-devel >= 5
BuildRequires:	Qt5Test-devel >= 5
BuildRequires:	Qt5Xml-devel >= 5
BuildRequires:	cryptsetup-devel
BuildRequires:	doxygen
BuildRequires:	libproxy-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Single Sign On libraries and daemon.

%description -l pl.UTF-8
Biblioteki i demon Single Sign On.

%package libs
Summary:	Single Sign On Qt-based libraries
Summary(pl.UTF-8):	Biblioteki Single Sign On oparte na Qt
Group:		Libraries

%description libs
Single Sign On Qt-based libraries.

%description libs -l pl.UTF-8
Biblioteki Single Sign On oparte na Qt.

%package devel
Summary:	Development files for Single Sign On libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek Single Sign On
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	Qt5Core-devel >= 5
Requires:	Qt5DBus-devel >= 5
Requires:	Qt5Sql-devel >= 5
# for signon-plugins.pc
Requires:	libsignon-qt-devel = %{version}-%{release}

%description devel
Development files for Single Sign On libraries.

%description devel -l pl.UTF-8
Pliki programistyczne bibliotek Single Sign On.

%package apidocs
Summary:	API documentation for Single Sign On daemon and libraries
Summary(pl.UTF-8):	Dokumentacja API demona i bibliotek Single Sign On
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for Single Sign On daemon and libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API demona i bibliotek Single Sign On.

%package -n libsignon-qt
Summary:	Client library for the Single Sign On daemon - Qt 4 bindings
Summary(pl.UTF-8):	Biblioteka kliencka demona Single Sign On - wiązania Qt 4
Group:		Libraries

%description -n libsignon-qt
Client library for the Single Sign On daemon - Qt 4 bindings.

%description -n libsignon-qt -l pl.UTF-8
Biblioteka kliencka demona Single Sign On - wiązania Qt 4.

%package -n libsignon-qt-devel
Summary:	Header files for Single Sign On daemon Qt 4 client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej Qt 4 demona Single Sign On
Group:		Development/Libraries
Requires:	QtCore-devel >= 4
Requires:	libsignon-qt = %{version}-%{release}

%description -n libsignon-qt-devel
Header files for Single Sign On daemon Qt 4 client library.

%description -n libsignon-qt-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej Qt 4 demona Single Sign On.

%package -n libsignon-qt-static
Summary:	Static libsignon-qt library
Summary(pl.UTF-8):	Statyczna biblioteka libsignon-qt
Group:		Development/Libraries
Requires:	libsignon-qt-devel = %{version}-%{release}

%description -n libsignon-qt-static
Static libsignon-qt library.

%description -n libsignon-qt-static -l pl.UTF-8
Statyczna biblioteka libsignon-qt.

%package -n libsignon-qt-apidocs
Summary:	API documentation for Single Sign On daemon Qt client library
Summary(pl.UTF-8):	Dokumentacja API biblioteki klienckiej Qt demona Single Sign On
Group:		Documentation

%description -n libsignon-qt-apidocs
API documentation for Single Sign On daemon Qt client library.

%description -n libsignon-qt-apidocs -l pl.UTF-8
Dokumentacja API biblioteki klienckiej Qt demona Single Sign On.

%package -n libsignon-qt5
Summary:	Client library for the Single Sign On daemon - Qt 5 bindings
Summary(pl.UTF-8):	Biblioteka kliencka demona Single Sign On - wiązania Qt 5
Group:		Libraries

%description -n libsignon-qt5
Client library for the Single Sign On daemon - Qt 5 bindings.

%description -n libsignon-qt5 -l pl.UTF-8
Biblioteka kliencka demona Single Sign On - wiązania Qt 5.

%package -n libsignon-qt5-devel
Summary:	Header files for Single Sign On daemon Qt 5 client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej Qt 5 demona Single Sign On
Group:		Development/Libraries
Requires:	Qt5Core-devel >= 5
Requires:	libsignon-qt5 = %{version}-%{release}

%description -n libsignon-qt5-devel
Header files for Single Sign On daemon Qt 5 client library.

%description -n libsignon-qt5-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej Qt 5 demona Single Sign On.

%package -n libsignon-qt5-static
Summary:	Static libsignon-qt5 library
Summary(pl.UTF-8):	Statyczna biblioteka libsignon-qt5
Group:		Development/Libraries
Requires:	libsignon-qt5-devel = %{version}-%{release}

%description -n libsignon-qt5-static
Static libsignon-qt5 library.

%description -n libsignon-qt5-static -l pl.UTF-8
Statyczna biblioteka libsignon-qt5.

%prep
%setup -q -n signond-VERSION_%{version}-aa1bcf3c9218addbdb376a40151b689409046125
%patch0 -p1

%build
install -d build-qt5
cd build-qt5
qmake-qt5 ../signon.pro \
	CONFIG+=cryptsetup \
	BUILD_DIR="build-qt5" \
	LIBDIR="%{_libdir}" \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}
cd ..

%if %{with qt4}
install -d build-qt4/lib/SignOn
cd build-qt4/lib/SignOn
qmake-qt4 ../../../lib/SignOn/SignOn.pro \
	CONFIG+=cryptsetup \
	BUILD_DIR="build-qt4" \
	LIBDIR="%{_libdir}" \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%{__make} -C build-qt4/lib/SignOn install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

%{__make} -C build-qt5 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.so.1.?

install -d $RPM_BUILD_ROOT%{_docdir}/signon-apidocs-%{version} \
	$RPM_BUILD_ROOT%{_examplesdir}/signon-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/libsignon-qt/html $RPM_BUILD_ROOT%{_docdir}/libsignon-qt-apidocs-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/signon/html $RPM_BUILD_ROOT%{_docdir}/signon-apidocs-%{version}/signon
%{__mv} $RPM_BUILD_ROOT%{_docdir}/signon-plugins/html $RPM_BUILD_ROOT%{_docdir}/signon-apidocs-%{version}/signon-plugins
%{__mv} $RPM_BUILD_ROOT%{_docdir}/signon-plugins-dev/example $RPM_BUILD_ROOT%{_examplesdir}/signon-%{version}/signon-plugins

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n libsignon-qt -p /sbin/ldconfig
%postun	-n libsignon-qt -p /sbin/ldconfig

%post	-n libsignon-qt5 -p /sbin/ldconfig
%postun	-n libsignon-qt5 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/signond.conf
%attr(755,root,root) %{_bindir}/signond
%attr(755,root,root) %{_bindir}/signonpluginprocess
%dir %{_libdir}/signon
%attr(755,root,root) %{_libdir}/signon/libexampleplugin.so
%attr(755,root,root) %{_libdir}/signon/libpasswordplugin.so
%attr(755,root,root) %{_libdir}/signon/libssotestplugin.so
%attr(755,root,root) %{_libdir}/signon/libssotest2plugin.so
%dir %{_libdir}/signon/extensions
%attr(755,root,root) %{_libdir}/signon/extensions/libcryptsetup.so
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.SingleSignOn.service
%{_datadir}/dbus-1/services/com.nokia.SingleSignOn.Backup.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-extension.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsignon-extension.so.1
%attr(755,root,root) %{_libdir}/libsignon-plugins.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsignon-plugins.so.1
%attr(755,root,root) %{_libdir}/libsignon-plugins-common.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsignon-plugins-common.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-extension.so
%attr(755,root,root) %{_libdir}/libsignon-plugins.so
%attr(755,root,root) %{_libdir}/libsignon-plugins-common.so
%{_includedir}/signon-extension
%{_includedir}/signon-plugins
%{_includedir}/signond
%{_pkgconfigdir}/SignOnExtension.pc
%{_pkgconfigdir}/signon-plugins.pc
%{_pkgconfigdir}/signon-plugins-common.pc
%{_pkgconfigdir}/signond.pc
%{_datadir}/dbus-1/interfaces/com.google.code.AccountsSSO.SingleSignOn.AuthService.xml
%{_datadir}/dbus-1/interfaces/com.google.code.AccountsSSO.SingleSignOn.AuthSession.xml
%{_datadir}/dbus-1/interfaces/com.google.code.AccountsSSO.SingleSignOn.Identity.xml

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/signon-apidocs-%{version}
%{_examplesdir}/signon-%{version}

%if %{with qt4}
%files -n libsignon-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-qt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsignon-qt.so.1

%files -n libsignon-qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-qt.so
%{_includedir}/signon-qt
%{_pkgconfigdir}/libsignon-qt.pc
%{_libdir}/cmake/SignOnQt

%files -n libsignon-qt-static
%defattr(644,root,root,755)
%{_libdir}/libsignon-qt.a

%files -n libsignon-qt-apidocs
%defattr(644,root,root,755)
%{_docdir}/libsignon-qt-apidocs-%{version}
%endif

%files -n libsignon-qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsignon-qt5.so.1

%files -n libsignon-qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-qt5.so
%{_includedir}/signon-qt5
%{_pkgconfigdir}/libsignon-qt5.pc
%{_libdir}/cmake/SignOnQt5

%files -n libsignon-qt5-static
%defattr(644,root,root,755)
%{_libdir}/libsignon-qt5.a
