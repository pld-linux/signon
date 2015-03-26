#
# Conditional build:
%bcond_without	qt5	# libsignon-qt5 binding

Summary:	Single Sign On libraries and daemon
Summary(pl.UTF-8):	Biblioteki i demon Single Sign On
Name:		signon
Version:	8.56
Release:	3
License:	LGPL v2.1
Group:		Libraries
#Source0Download: http://code.google.com/p/accounts-sso/downloads/list
Source0:	http://accounts-sso.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	85ac10ab581d84ec2344a42349bc693b
Patch0:		%{name}-cryptsetup.patch
Patch1:		%{name}-link.patch
URL:		http://code.google.com/p/accounts-sso/
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5DBus-devel >= 5
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
%endif
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtDBus-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	QtNetwork-devel >= 4
BuildRequires:	QtSql-devel >= 4
BuildRequires:	QtTest-devel >= 4
BuildRequires:	QtXml-devel >= 4
BuildRequires:	cryptsetup-devel
BuildRequires:	doxygen
BuildRequires:	libproxy-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
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
Requires:	QtCore-devel >= 4
Requires:	QtDBus-devel >= 4
Requires:	QtSql-devel >= 4
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
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build-qt4
cd build-qt4
qmake-qt4 ../signon.pro \
	CONFIG+=cryptsetup \
	BUILD_DIR="build-qt4" \
	LIBDIR="%{_libdir}" \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}
cd ..

%if %{with qt5}
install -d build-qt5/lib/SignOn
cd build-qt5/lib/SignOn
qmake-qt5 ../../../lib/SignOn/SignOn.pro \
	CONFIG+=cryptsetup \
	BUILD_DIR="build-qt5" \
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
%{__make} -C build-qt5/lib/SignOn install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# separate from qt4 version
%{__mv} $RPM_BUILD_ROOT%{_libdir}/cmake/{SignOnQt,SignOnQt5}
%{__mv} $RPM_BUILD_ROOT%{_libdir}/cmake/SignOnQt5/{SignOnQt,SignOnQt5}Config.cmake
%{__mv} $RPM_BUILD_ROOT%{_libdir}/cmake/SignOnQt5/{SignOnQt,SignOnQt5}ConfigVersion.cmake
%endif

%{__make} -C build-qt4 install \
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
%attr(755,root,root) %{_libdir}/libsignon-plugins-common.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsignon-plugins-common.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-extension.so
%attr(755,root,root) %{_libdir}/libsignon-plugins-common.so
%{_libdir}/libsignon-plugins.a
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

%if %{with qt5}
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
%endif
