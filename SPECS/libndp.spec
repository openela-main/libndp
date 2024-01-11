Name: libndp
Version: 1.7
Release: 6%{?dist}
Summary: Library for Neighbor Discovery Protocol
Group: System Environment/Libraries
License: LGPLv2+
URL: http://www.libndp.org/
Source: http://www.libndp.org/files/libndp-%{version}.tar.gz

Patch1: 0001-ndptool-add-T-target-support.patch
Patch2: 0002-ndptool-fix-target-parameter-typo.patch
Patch3: 0003-libndp-close-sockfd-after-using-to-avoid-handle-leak.patch
Patch4: 0004-libndp-fix-nd_msg-typo-when-setting-target-address.patch
Patch5: 0005-ndptool-add-D-dest-support.patch
Patch6: 0006-ndptool-fix-potential-memory-leak-caused-by-strdup.patch
Patch7: 0007-libndp-ndptool-use-poll-instead-of-select.patch

%description
This package contains a library which provides a wrapper
for IPv6 Neighbor Discovery Protocol.  It also provides a tool
named ndptool for sending and receiving NDP messages.

%package devel
Group: Development/Libraries
Summary: Libraries and header files for libndp development
Requires: libndp = %{version}-%{release}

%description devel
The libndp-devel package contains the header files and libraries
necessary for developing programs using libndp.

%prep
%setup -q
%patch1 -p1 -b .ndptool_add_T_target_support
%patch2 -p1 -b .ndptool_fix_target_parameter_typo
%patch3 -p1 -b .libndp_close_sockfd_after_using
%patch4 -p1 -b .libndp_fix_nd_msg_typo
%patch5 -p1 -b .ndptool_add_D_dest_support
%patch6 -p1 -b .ndptool_fix_potential_memory_leak
%patch7 -p1 -b .ndptool_use_poll

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name \*.la -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_libdir}/*so.*
%{_bindir}/ndptool
%{_mandir}/man8/ndptool.8*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Apr 26 2021 Hangbin Liu <haliu@redhat.com> - 1.7-6
- Bump the version number due to conflict with (rhbz 1937721)

* Fri Mar 12 2021 Hangbin Liu <haliu@redhat.com> - 1.7-5
- Bump the version number due to conflict with (rhbz 1937721)

* Fri Mar 05 2021 Hangbin Liu <haliu@redhat.com> - 1.7-4
- libndp,ndptool: use poll() instead of select (rhbz 1933041)

* Fri Nov 01 2019 Hangbin Liu <haliu@redhat.com> - 1.7-3
- ndptool: add -D dest support (rhbz 1697595)
- ndptool: fix potential memory leak caused by strdup (rhbz 1697595)

* Fri Nov 01 2019 Hangbin Liu <haliu@redhat.com> - 1.7-2
- ndptool: add -T target support (rhbz 1666194)
- ndptool: fix target parameter typo (rhbz 1666194)
- libndp: close sockfd after using to avoid handle leak (rhbz 1666194)
- libndp: fix nd_msg typo when setting target address (rhbz 1666194)

* Thu Jul 18 2019 Hangbin Liu <haliu@redhat.com> - 1.7-1
- Update to 1.7
- libndp: apply filter to raw socket to only accept ND messages
- libndp: move ndp_sock_{open,close}() after msg parsing functions
- ndptool: Fix compilation on musl libc

* Tue Jul 16 2019 Hangbin Liu <haliu@redhat.com> - 1.6-7
- Add libndp gating test (rhbz 1682325)

* Fri Sep 28 2018 Eric Garver <egarver@redhat.com> - 1.6-6
- Rebuilt for annocheck fixes (rhbz 1630584)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jiri Pirko <jiri@mellanox.com> - 1.6-1
- Update to 1.6
- libndb: reject redirect and router advertisements from non-link-local
- libndp: validate the IPv6 hop limit
- libndp: revert API change for ndp_msg_send() and add ndp_msg_send_with_flags()
- libndp: fix type of field "na" in "struct ndp_msgna"
- ndptool: add option to send messages types
- libndp: add option flags to send messages
- Add SubmittingPatches howto

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 02 2015 Jiri Pirko <jpirko@redhat.com> - 1.5-1
- Update to 1.5
- ndptool: use conventional signal handlers instead of signalfd

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.4-3
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Jiri Pirko <jpirko@redhat.com> - 1.4-1
- Update to 1.4
- libndp: fix buffer overflow in ndp_msg_opt_dnssl_domain()

* Thu Jun 26 2014 Jiri Pirko <jpirko@redhat.com> - 1.3-1
- Update to 1.3
- Add missing <stdarg.h> include for va_list

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Jiri Pirko <jpirko@redhat.com> - 1.2-2
- libndp: fix [cppcheck] Undefined behavior: Variable 'buf' is used as parameter and destination in s[n]printf() [1044084] [1091720]

* Tue Oct 15 2013 Jiri Pirko <jpirko@redhat.com> - 1.2-1
- Update to 1.2
- libndp: silently ignore packets with optlen 0
- libndp: fix processing for larger options
- libndp: do not fail on receiving non-ndp packets

* Fri Oct 04 2013 Jiri Pirko <jpirko@redhat.com> - 1.1-1
- Update to 1.1

* Fri Sep 13 2013 Dan Williams <dcbw@redhat.com> - 1.0-2
- Fix .pc file includes path
- Fix ndptool -v argument

* Thu Aug 08 2013 Jiri Pirko <jpirko@redhat.com> - 1.0-1
- Update to 1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4.20130723git873037a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Dan Williams <dcbw@redhat.com> - 0.1-3.20130723git873037a
- Update to git 873037a

* Fri Jun 07 2013 Jiri Pirko <jpirko@redhat.com> - 0.1-2.20130607git39e1f53
- Update to git 39e1f53

* Sat May 04 2013 Jiri Pirko <jpirko@redhat.com> - 0.1-1.20130504gitca3c399
- Initial build.
