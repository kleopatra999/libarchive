#
# Conditional build:
%bcond_without	static_libs # don't build static libraries

Summary:	Multi-format archive and compression library
Summary(pl.UTF-8):	Biblioteka do archiwizacji i kompresji w wielu formatach
Name:		libarchive
Version:	3.2.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.libarchive.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	596210b5a9c2ff74a0f7ca34838d655f
Patch0:		%{name}-man_progname.patch
URL:		http://www.libarchive.org/
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	bzip2-devel
# for <ext2fs/ext2_fs.h>
BuildRequires:	e2fsprogs-devel
BuildRequires:	libxml2-devel >= 2
BuildRequires:	lz4-devel >= r131
BuildRequires:	lzo-devel >= 2
BuildRequires:	nettle-devel
BuildRequires:	pkgconfig
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Requires:	lz4-libs >= r131
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular TAR
variants, several CPIO formats, and both BSD and GNU ar variants. It
can also write SHAR archives and read ISO9660 CDROM images and ZIP
archives.

See README for complete format support.

%description -l pl.UTF-8
Libarchive to biblioteka potrafiąca tworzyć i odczytywać kilka różnych
formatów archiwów strumieniowych, w tym najbardziej popularne warianty
archiwów TAR, kilka formatów CPIO oraz warianty BSD oraz GNU archiwów
ar. Potrafi także zapisywać archiwa SHAR oraz odczytywać obrazy CDROM
ISO9660 i archiwa ZIP.

Pełny wykaz obsługiwanych formatów znajduje się w pliku README.

%package devel
Summary:	Header files for libarchive library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libarchive
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	acl-devel
Requires:	attr-devel
Requires:	bzip2-devel
Requires:	libxml2-devel
Requires:	lz4-devel >= r131
Requires:	nettle-devel
Requires:	xz-devel
Requires:	zlib-devel

%description devel
Header files for libarchive library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libarchive.

%package static
Summary:	Static libarchive library
Summary(pl.UTF-8):	Statyczna biblioteka libarchive
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libarchive library.

%description static -l pl.UTF-8
Statyczna biblioteka libarchive.

%package -n bsdcat
Summary:	bsdcat - cat(1) implementation based on libarchive
Summary(pl.UTF-8):	bsdcat - implementacja programu cat(1) oparta na libarchive
Group:		Applications/Archiving
Requires:	%{name} = %{version}-%{release}

%description -n bsdcat
bsdcat - cat(1) implementation based on libarchive.

%description -n bsdcat -l pl.UTF-8
bsdcat - implementacja programu cat(1), oparta na libarchive.

%package -n bsdcpio
Summary:	bsdcpio - cpio(1) implementation based on libarchive
Summary(pl.UTF-8):	bsdcpio - implementacja programu cpio(1) oparta na libarchive
Group:		Applications/Archiving
Requires:	%{name} = %{version}-%{release}

%description -n bsdcpio
bsdcpio - cpio(1) implementation based on libarchive.

%description -n bsdcpio -l pl.UTF-8
bsdcpio - implementacja programu cpio(1), oparta na libarchive.

%package -n bsdtar
Summary:	bsdtar - tar(1) implementation based on libarchive
Summary(pl.UTF-8):	bsdtar - implementacja programu tar(1) oparta na libarchive
Group:		Applications/Archiving
Requires:	%{name} = %{version}-%{release}

%description -n bsdtar
bsdtar - tar(1) implementation based on libarchive.

%description -n bsdtar -l pl.UTF-8
bsdtar - implementacja programu tar(1), oparta na libarchive.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules \
	--enable-bsdcat=shared \
	--enable-bsdcpio=shared \
	--enable-bsdtar=shared \
	--enable-static%{!?with_static_libs:=no}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS COPYING
%attr(755,root,root) %{_libdir}/libarchive.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libarchive.so.13

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarchive.so
%{_libdir}/libarchive.la
%{_includedir}/archive*.h
%{_mandir}/man3/archive_*.3*
%{_mandir}/man3/libarchive.3*
%{_mandir}/man3/libarchive_changes.3*
%{_mandir}/man3/libarchive_internals.3*
%{_mandir}/man5/libarchive-formats.5*
%{_mandir}/man5/cpio.5*
%{_mandir}/man5/mtree.5*
%{_mandir}/man5/tar.5*
%{_pkgconfigdir}/libarchive.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libarchive.a
%endif

%files -n bsdcat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bsdcat
%{_mandir}/man1/bsdcat.1*

%files -n bsdcpio
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bsdcpio
%{_mandir}/man1/bsdcpio.1*

%files -n bsdtar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bsdtar
%{_mandir}/man1/bsdtar.1*
