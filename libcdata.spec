Summary:	Library for cross-platform C generic data functions
Summary(pl.UTF-8):	Biblioteka wieloplatformowych funkcji ogólnej obsługi danych w C
Name:		libcdata
# version from AC_INIT
Version:	20150102
%define	gitrev	1ae7a100d49d52a17b24c57efc941c9370be0ea8
Release:	2
License:	LGPL v3+
Group:		Libraries
#Source0:	https://github.com/libyal/libcdata/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/libyal/libcdata/archive/%{gitrev}/%{name}-%{version}.tar.gz
# Source0-md5:	c85b2ddc9c585114a1c40f99df8b4f8c
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libcdata/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcthreads-devel >= 20130509
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcerror >= 20120425
Requires:	libcstring >= 20120425
Requires:	libcthreads >= 20130509
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
Requires:	libcerror-devel >= 20120425
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= 20130509

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
%setup -q -n %{name}-%{gitrev}
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
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
