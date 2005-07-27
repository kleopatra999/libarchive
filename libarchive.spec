Summary:	Library to create and read several different archive formats
Summary(pl):	Biblioteka do tworzenia i odczytu r�nych format�w archiw�w
Name:		libarchive
Version:	1.02.027
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://people.freebsd.org/~kientzle/libarchive/src/%{name}-%{version}.tar.gz
# Source0-md5:	b59180f515666e65b4338f3b1ec1f53e
Patch0:		%{name}-shared.patch
URL:		http://people.freebsd.org/~kientzle/libarchive/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular TAR
variants and several CPIO formats. It can also write SHAR archives.

%description -l pl
Libarchive jest bibliotek� s�u�ac� to tworzenia i odczytu wielu
r�nych strumieniowych format�w archiw�w, w��czaj�c w to popularne
odmiany TAR oraz wiele format�w CPIO. Biblioteka ta poptrafi tak�e
zapisywa� archiwa SHAR.

%package devel
Summary:	Header files for libarchive library
Summary(pl):	Pliki nag��wkowe biblioteki libarchive
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libarchive library.

%description devel -l pl
Pliki nag��wkowe biblioteki libarchive.

%package static
Summary:	Static libarchive library
Summary(pl):	Statyczna biblioteka libarchive
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libarchive library.

%description static -l pl
Statyczna biblioteka libarchive.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	LDFLAGS="%{rpmldflags} -lz -lbz2"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libarchive.so.*.*.* $RPM_BUILD_ROOT%{_libdir}/libarchive.so

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarchive.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarchive.so
%{_libdir}/libarchive.la
%{_includedir}/*.h
%{_mandir}/man3/*
%{_mandir}/man5/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libarchive.a

%clean
rm -rf $RPM_BUILD_ROOT
