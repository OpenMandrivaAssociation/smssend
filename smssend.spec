%define name    smssend
%define version 3.4
%define release 11

Summary: 	Send free SMS to any GSM
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.bz2
URL: 		http://zekiller.skytech.org/smssend_menu_en.html 
License: 	GPL 
Group: 		Networking/Other
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:  skyutils-devel openssl-devel zlib-devel 
BuildRequires:  bzip2-devel pcre-devel

%description
SmsSend allows you to send free SMS to any GSM, connecting to Internet sites
using scripts. It is available both for Windows and Unix.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README INSTALL
%doc NEWS
%_bindir/*
%_mandir/man1/*
%_datadir/%name/
%lang(fr) %_mandir/fr/man1/*


%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 3.4-10mdv2012.0
+ Revision: 773076
- relink against libpcre.so.1

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 3.4-9mdv2011.0
+ Revision: 614930
- the mass rebuild of 2010.1 packages

* Mon Feb 22 2010 Funda Wang <fwang@mandriva.org> 3.4-8mdv2010.1
+ Revision: 509843
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 3.4-4mdv2008.1
+ Revision: 140829
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 10 2007 Pascal Terjan <pterjan@mandriva.org> 3.4-4mdv2008.0
+ Revision: 61371
- Rebuild
- Import smssend



* Thu Apr 20 2006 Lenny Cartier <lenny@mandrakesoft.com> 3.4-3mdk
- rebuild for dependencies

* Wed Aug 17 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.4-2mdk
- rebuild for las skyutils

* Wed Feb 02 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.4-1mdk
- 3.4

* Thu Dec 25 2003 Pascal Terjan <CMoi@tuxfamily.org> 3.3-1mdk
- 3.3

* Sun Dec 21 2003 Pascal Terjan <CMoi@tuxfamily.org> 3.2-4mdk
- rebuild for new libskyutils

* Fri Dec 12 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.2-3mdk
- fix buildrequires (lib64..)
- drop explicit library dependency
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- quiet setup

* Fri Apr 25 2003 Pascal Terjan <CMoi@tuxfamily.org> 3.2-2mdk
- add some buildrequires 

* Sun Mar 02 2003 Pascal Terjan <CMoi@tuxfamily.org> 3.2-1mdk
- 3.2 

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.1-2mdk
- rebuild

* Tue Apr 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 3.1-1mdk
- 3.1

* Thu Jan 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.9-2mdk
- fix requires & buildrequires

* Tue Nov 27 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.9-1mdk
- 2.9

* Fri Nov 16 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.8-1mdk
- 2.8

* Tue Aug 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.7-1mdk
- 2.7

* Tue Apr 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.6-1mdk
- updated by Christian Zoffoli <czoffoli@linux-mandrake.com> :
	- 2.6

* Mon Feb 26 2001 Christian Zoffoli <czoffoli@linux-mandrake.com> 2.5-1mdk
- updated to 2.5

* Mon Jan 29 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.4-1mdk
- updated to 2.4

* Wed Jan 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.3-1mdk
- updated to 2.3

* Tue Dec 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.1-1mdk
- new in contribs
