#
# Conditional build:
%bcond_with	cryptsetup		# cryptsetup support
%bcond_without	qt5			# qt5 version
%bcond_without	qt6			# qt6 version

%define snapshot 20240113
#
Summary:	Single Sign On libraries and daemon
Summary(pl.UTF-8):	Biblioteki i demon Single Sign On
Name:		signon
Version:	8.62
Release:	2.%{snapshot}
License:	LGPL v2.1
Group:		Libraries
# Original version: https://gitlab.com/accounts-sso/signond
# But the fork is better and more actively maintained.
#Source0Download: https://gitlab.com/nicolasfella/signond/tags
Source0:	https://gitlab.com/nicolasfella/signond/-/archive/qt6/signond-qt6.tar.bz2
# Source0-md5:	af002cbaf35c77d751c484ac1c8b0206
# submodule
Source1:	https://gitlab.com/accounts-sso/signon-dbus-specification/-/archive/67487954653006ebd0743188342df65342dc8f9b/signon-dbus-specification-67487954653006ebd0743188342df65342dc8f9b.tar.bz2
# Source1-md5:	21f2a3bf51a6c7eb6f74a2d3c776fcb9
Patch0:		%{name}-cryptsetup.patch
URL:		https://gitlab.com/nicolasfella/signond
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5DBus-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Network-devel >= 5
BuildRequires:	Qt5Sql-devel >= 5
BuildRequires:	Qt5Test-devel >= 5
BuildRequires:	Qt5Xml-devel >= 5
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
%endif
%if %{with qt6}
BuildRequires:	Qt6Core-devel >= 6
BuildRequires:	Qt6DBus-devel >= 6
BuildRequires:	Qt6Gui-devel >= 6
BuildRequires:	Qt6Network-devel >= 6
BuildRequires:	Qt6Sql-devel >= 6
BuildRequires:	Qt6Test-devel >= 6
BuildRequires:	Qt6Xml-devel >= 6
BuildRequires:	qt6-build >= 6
BuildRequires:	qt6-qmake >= 6
%endif
%{?with_cryptsetup:BuildRequires:	cryptsetup-devel}
BuildRequires:	doxygen
BuildRequires:	libproxy-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
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
%if %{with qt6}
Requires:	Qt6Core-devel >= 6
Requires:	Qt6DBus-devel >= 6
Requires:	Qt6Sql-devel >= 6
# for signon-plugins.pc
Requires:	libsignon-qt6-devel = %{version}-%{release}
%else
Requires:	Qt5Core-devel >= 5
Requires:	Qt5DBus-devel >= 5
Requires:	Qt5Sql-devel >= 5
# for signon-plugins.pc
Requires:	libsignon-qt5-devel = %{version}-%{release}
%endif

%description devel
Development files for Single Sign On libraries.

%description devel -l pl.UTF-8
Pliki programistyczne bibliotek Single Sign On.

%package apidocs
Summary:	API documentation for Single Sign On daemon and libraries
Summary(pl.UTF-8):	Dokumentacja API demona i bibliotek Single Sign On
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Single Sign On daemon and libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API demona i bibliotek Single Sign On.

%package -n libsignon-qt-apidocs
Summary:	API documentation for Single Sign On daemon Qt client library
Summary(pl.UTF-8):	Dokumentacja API biblioteki klienckiej Qt demona Single Sign On
Group:		Documentation
BuildArch:	noarch

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

%package -n libsignon-qt6
Summary:	Client library for the Single Sign On daemon - Qt 6 bindings
Summary(pl.UTF-8):	Biblioteka kliencka demona Single Sign On - wiązania Qt 6
Group:		Libraries

%description -n libsignon-qt6
Client library for the Single Sign On daemon - Qt 6 bindings.

%description -n libsignon-qt6 -l pl.UTF-8
Biblioteka kliencka demona Single Sign On - wiązania Qt 6.

%package -n libsignon-qt6-devel
Summary:	Header files for Single Sign On daemon Qt 6 client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej Qt 6 demona Single Sign On
Group:		Development/Libraries
Requires:	Qt6Core-devel >= 6
Requires:	libsignon-qt6 = %{version}-%{release}

%description -n libsignon-qt6-devel
Header files for Single Sign On daemon Qt 6 client library.

%description -n libsignon-qt6-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej Qt 6 demona Single Sign On.

%package -n libsignon-qt6-static
Summary:	Static libsignon-qt6 library
Summary(pl.UTF-8):	Statyczna biblioteka libsignon-qt6
Group:		Development/Libraries
Requires:	libsignon-qt6-devel = %{version}-%{release}

%description -n libsignon-qt6-static
Static libsignon-qt6 library.

%description -n libsignon-qt6-static -l pl.UTF-8
Statyczna biblioteka libsignon-qt6.

%prep
%setup -q -n signond-qt6
tar xf %{SOURCE1} -C lib/signond/interfaces --strip-components 1
%patch -P 0 -p1

# disable docs in qch format (signon.qch)
%{__sed} -i -e '/GENERATE_QHP/ s/YES/NO/' doc/doxy.conf lib/SignOn/doc/doxy.conf lib/plugins/doc/doxy.conf
%{__sed} -i -e '/doc\/qch/d' doc/doc.pri lib/SignOn/doc/doc.pri lib/plugins/doc/doc.pri

%build
%if %{with qt5}
install -d build-qt5
cd build-qt5
qmake-qt5 ../signon.pro \
	%{?with_cryptsetup:CONFIG+=cryptsetup} \
	BUILD_DIR="build-qt5" \
	LIBDIR="%{_libdir}" \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}
cd ..
%endif

%if %{with qt6}
install -d build-qt6
cd build-qt6
qmake-qt6 ../signon.pro \
	%{?with_cryptsetup:CONFIG+=cryptsetup} \
	BUILD_DIR="build-qt6" \
	LIBDIR="%{_libdir}" \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt5}
%{__make} -C build-qt5 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

%if %{with qt6}
%{__make} -C build-qt6 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.so.1.?

install -d $RPM_BUILD_ROOT%{_docdir}/signon-apidocs-%{version} \
	$RPM_BUILD_ROOT%{_examplesdir}/signon-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/libsignon-qt/html $RPM_BUILD_ROOT%{_docdir}/libsignon-qt-apidocs-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/signon/html $RPM_BUILD_ROOT%{_docdir}/signon-apidocs-%{version}/signon
%{__mv} $RPM_BUILD_ROOT%{_docdir}/signon-plugins/html $RPM_BUILD_ROOT%{_docdir}/signon-apidocs-%{version}/signon-plugins
%{__mv} $RPM_BUILD_ROOT%{_docdir}/signon-plugins-dev/example $RPM_BUILD_ROOT%{_examplesdir}/signon-%{version}/signon-plugins

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n libsignon-qt5 -p /sbin/ldconfig
%postun	-n libsignon-qt5 -p /sbin/ldconfig

%post	-n libsignon-qt6 -p /sbin/ldconfig
%postun	-n libsignon-qt6 -p /sbin/ldconfig

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
%if %{with cryptsetup}
%dir %{_libdir}/signon/extensions
%attr(755,root,root) %{_libdir}/signon/extensions/libcryptsetup.so
%endif
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.SingleSignOn.service
%{_datadir}/dbus-1/services/com.nokia.SingleSignOn.Backup.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-extension.so.*.*.*
%ghost %{_libdir}/libsignon-extension.so.1
%attr(755,root,root) %{_libdir}/libsignon-plugins.so.*.*.*
%ghost %{_libdir}/libsignon-plugins.so.1
%attr(755,root,root) %{_libdir}/libsignon-plugins-common.so.*.*.*
%ghost %{_libdir}/libsignon-plugins-common.so.1
%dir %{_libdir}/%{name}/extensions

%files devel
%defattr(644,root,root,755)
%{_libdir}/libsignon-extension.so
%{_libdir}/libsignon-plugins.so
%{_libdir}/libsignon-plugins-common.so
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

%files -n libsignon-qt-apidocs
%defattr(644,root,root,755)
%{_docdir}/libsignon-qt-apidocs-%{version}

%if %{with qt5}
%files -n libsignon-qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-qt5.so.*.*.*
%ghost %{_libdir}/libsignon-qt5.so.1

%files -n libsignon-qt5-devel
%defattr(644,root,root,755)
%{_libdir}/libsignon-qt5.so
%{_includedir}/signon-qt5
%{_pkgconfigdir}/libsignon-qt5.pc
%{_libdir}/cmake/SignOnQt5

%files -n libsignon-qt5-static
%defattr(644,root,root,755)
%{_libdir}/libsignon-qt5.a
%endif

%if %{with qt6}
%files -n libsignon-qt6
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-qt6.so.*.*.*
%ghost %{_libdir}/libsignon-qt6.so.1

%files -n libsignon-qt6-devel
%defattr(644,root,root,755)
%{_libdir}/libsignon-qt6.so
%{_includedir}/signon-qt6
%{_pkgconfigdir}/libsignon-qt6.pc
%{_libdir}/cmake/SignOnQt6

%files -n libsignon-qt6-static
%defattr(644,root,root,755)
%{_libdir}/libsignon-qt6.a
%endif
