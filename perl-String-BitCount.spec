%include	/usr/lib/rpm/macros.perl
Summary:	String-BitCount perl module
Summary(pl):	Modu³ perla String-BitCount
Name:		perl-String-BitCount
Version:	1.11
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/String/String-BitCount-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String-BitCount - counts number of "1" bits in string.

%description -l pl
String-BitCount - zlicza ilo¶æ bitów "1" w ³añcuchu.

%prep
%setup -q -n String-BitCount-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/String/BitCount
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/String/BitCount.pm
%{perl_sitearch}/auto/String/BitCount

%{_mandir}/man3/*
