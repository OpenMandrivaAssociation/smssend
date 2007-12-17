%define name    smssend
%define version 3.4
%define release %mkrel 4

Summary: 	Send free SMS to any GSM
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.bz2
URL: 		http://zekiller.skytech.org/smssend_menu_en.html 
License: 	GPL 
Group: 		Networking/Other
Buildrequires:  skyutils-devel openssl-devel zlib-devel 
BuildRequires:  bzip2-devel pcre-devel

%description
SmsSend allows you to send free SMS to any GSM, connecting to Internet sites
using scripts. It is available both for Windows and Unix.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

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
