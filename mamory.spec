Name:           mamory
Version:        0.2.25
Release:        31%{?dist}
Summary:        ROM management API and commandline ROM manager for MAME
License:        GPLv2 and LGPLv2
URL:            http://mamory.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         %{name}-opt.patch
Patch1:         %{name}-0.2.25-ppc64.patch
Patch2:         %{name}-0.2.25-utf8.patch
Patch3:         %{name}-0.2.25-fix-inline-use.patch
Patch4:         %{name}-0.2.25-type-cast.patch
Patch5:         %{name}-0.2.25-C23-support-strict-function-prototype-check.patch
BuildRequires:  expat-devel
BuildRequires:  gcc

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
%patch -P0 -p0 -b .opt~
%patch -P1 -p0 -b .ppc64~
%patch -P2 -p0 -b .utf8~
%patch -P3 -p1
%patch -P4 -p1 -b .cast
%patch -P5 -p1 -b .c23

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
%make_install

# remove libtool archive file
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%check
make check


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc AUTHORS ChangeLog COPYING TODO DOCS/mamory*
%{_bindir}/mamory
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so


%changelog
* Mon Feb 02 2026 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.25-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.25-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Feb 02 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.25-29
- Support C23 strict function prototype

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.25-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 13 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.25-27
- Fix -Werror=incompatible-pointer-types , cast return type properly

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.25-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.25-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.25-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.25-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.25-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.25-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.25-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.25-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.25-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.25-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.25-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.25-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.2.25-14
- Rebuilt

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.2.25-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.2.25-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.2.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 26 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.2.25-10
- clean up build flags

* Tue Jul 26 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.2.25-9
- Rebuild this dinosaur with the proper fedora build flags

* Sat May 16 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 0.2.25-8
- Fix FTBFS (rf#3626)

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.2.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.2.25-6
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.2.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.2.25-4
- rebuild for new F11 features

* Wed Oct 15 2008 Christopher Stone <chris.stone@gmail.com> 0.2.25-3
- Convert mamory.c to UTF-8 format

* Sun Oct 12 2008 Christopher Stone <chris.stone@gmail.com> 0.2.25-2
- Add patch for ppc64 compiles
- Clean up %%changelog

* Sun Nov 25 2007 Christopher Stone <chris.stone@gmail.com> 0.2.25-1
- Upstream sync
- Fix up some rpmlint warnings

* Mon Jul 30 2007 Christopher Stone <chris.stone@gmail.com> 0.2.24-1
- Upstream sync

* Wed Jan 17 2007 Christopher Stone <chris.stone@gmail.com> 0.2.23-1
- Upstream sync
- Rename patch file
- Add LGPL to license tag
- Remove COPYING from devel subpackage
- Improve summary tag
- Use rm instead of %%exclude
- Add expat-devel to BuildRequires
- Add dist tags to %%changelog

* Sat Dec 16 2006 Christopher Stone <chris.stone@gmail.com> 0.2.22-2
- Apply optimization patch from Belegdol

* Tue Dec 12 2006 Christopher Stone <chris.stone@gmail.com> 0.2.22-1
- Upstream sync

* Tue Dec 05 2006 Christopher Stone <chris.stone@gmail.com> 0.2.21-1
- Initial Release
