Summary:	DevHelp book: zvt
Summary(pl):	Ksi±¿ka do DevHelpa o zvt
Name:		devhelp-book-zvt
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/zvt.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp

%description
DevHelp book about zvt.

%description -l pl
Ksi±¿ka do DevHelpa o zvt.

%prep
%setup -q -c -n zvt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/zvt,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/zvt.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/zvt

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
