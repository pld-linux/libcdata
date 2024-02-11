# see m4/${libname}.m4 />= for required version of particular library
%define		libcerror_ver	20190308
%define		libcthreads_ver	20190308
Summary:	Library for cross-platform C generic data functions
Summary(pl.UTF-8):	Biblioteka wieloplatformowych funkcji ogólnej obsługi danych w C
Name:		libcdata
Version:	20240103
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libcdata/releases
Source0:	https://github.com/libyal/libcdata/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	de87cfb90704c81157c5c205dcb811cf
URL:		https://github.com/libyal/libcdata/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcthreads >= %{libcthreads_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcdata is a library for cross-platform C generic data functions.

%description -l pl.UTF-8
libcdata to biblioteka wieloplatformowych funkcji ogólnej obsługi
danych w C.

%package devel
Summary:	Header files for libcdata library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcdata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}

%description devel
Header files for libcdata library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcdata.

%package static
Summary:	Static libcdata library
Summary(pl.UTF-8):	Statyczna biblioteka libcdata
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcdata library.

%description static -l pl.UTF-8
Statyczna biblioteka libcdata.

%prep
%setup -q

%build
%{__gettextize}
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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcdata.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcdata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcdata.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdata.so
%{_includedir}/libcdata
%{_includedir}/libcdata.h
%{_pkgconfigdir}/libcdata.pc
%{_mandir}/man3/libcdata.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcdata.a
