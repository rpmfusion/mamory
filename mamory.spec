Name:           mamory
Version:        0.2.25
Release:        1%{?dist}
Summary:        ROM management API and commandline ROM manager for MAME

Group:          Applications/Emulators
License:        GPLv2 and LGPLv2
URL:            http://mamory.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         mamory-opt.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  expat-devel

%description
Mamory is a set of useful functions for emulators related projects.  It allows
easy inclusion of roms management features into these projects through a simple
API.

The distributed packages also contain a command line interface that use the
potential of the library libmamory.so.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains headers and libraries required to build applications that
use %{name}.


%prep
%setup -q
%patch0 -p0 -b .opt~

# Avoid lib64 rpaths
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure

# Fix file encodings
for file in AUTHORS DOCS/mamory.html DOCS/mamory.xml ; do
    iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
done


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# remove libtool archive file
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%check
make check


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO DOCS/mamory*
%{_bindir}/mamory
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/*.so


%changelog
* Sun Nov 25 2007 XulChris <tkmame@retrogames.com> 0.2.25-1%{?dist}
- Upstream sync
- Fix up some rpmlint warnings

* Mon Jul 30 2007 XulChris <tkmame@retrogames.com> 0.2.24-1%{?dist}
- Upstream sync

* Wed Jan 17 2007 XulChris <tkmame@retrogames.com> 0.2.23-1%{?dist}
- Upstream sync
- Rename patch file
- Add LGPL to license tag
- Remove COPYING from devel subpackage
- Improve summary tag
- Use rm instead of %%exclude
- Add expat-devel to BuildRequires
- Add dist tags to %%changelog

* Sat Dec 16 2006 XulChris <tkmame@retrogames.com> 0.2.22-2%{?dist}
- Apply optimization patch from Belegdol

* Tue Dec 12 2006 XulChris <tkmame@retrogames.com> 0.2.22-1%{?dist}
- Upstream sync

* Tue Dec 05 2006 XulChris <tkmame@retrogames.com> 0.2.21-1%{?dist}
- Initial Release
