%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	BitCount
Summary:	String::BitCount perl module
Summary(pl):	Modu³ perla String::BitCount
Name:		perl-String-BitCount
Version:	1.11
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::BitCount - counts number of "1" bits in string.

%description -l pl
String::BitCount - zlicza ilo¶æ bitów "1" w ³añcuchu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/String/BitCount.pm
%{_mandir}/man3/*
