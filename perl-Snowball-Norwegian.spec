%define upstream_name	 Snowball-Norwegian
%define upstream_version 1.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Porters stemming algorithm for Denmark
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/A/AS/ASKSH/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	locales-no
Obsoletes:	perl-Lingua-Stem-Snowball-No
Provides:	perl-Lingua-Stem-Snowball-No

%description
The stem function takes a scalar as a parameter and stems the word according to
Martin Porters Danish stemming algorithm, which can be found at the Snowball
website: http://snowball.tartarus.org/.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
