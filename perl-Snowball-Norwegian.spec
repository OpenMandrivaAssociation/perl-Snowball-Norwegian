%define module	Snowball-Norwegian
%define name	perl-%{module}
%define version 1.2
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Porters stemming algorithm for Denmark
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{module}/
Source:		http://search.cpan.org/CPAN/authors/id/A/AS/ASKSH/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Requires:	locales-no
Obsoletes:	perl-Lingua-Stem-Snowball-No
Provides:	perl-Lingua-Stem-Snowball-No
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The stem function takes a scalar as a parameter and stems the word according to
Martin Porters Danish stemming algorithm, which can be found at the Snowball
website: http://snowball.tartarus.org/.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Lingua
%{_bindir}/stemmer-no.pl
%{_mandir}/man3/*


