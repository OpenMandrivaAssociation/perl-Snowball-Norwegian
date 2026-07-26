%define upstream_name	 Snowball-Norwegian
Name:		perl-%{upstream_name}
Version:	1.2
Release:	6

Summary:	Porters stemming algorithm for Denmark
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        https://metacpan.org/dist/Snowball-Norwegian
Source0:	https://cpan.metacpan.org/authors/id/A/AS/ASKSH/Snowball-Norwegian-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel

BuildArch:	noarch
Requires:	locales-no
%rename perl-Lingua-Stem-Snowball-No

%description
The stem function takes a scalar as a parameter and stems the word according to
Martin Porters Danish stemming algorithm, which can be found at the Snowball
website: http://snowball.tartarus.org/.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Lingua
%{_bindir}/stemmer-no.pl
%{_mandir}/man3/*


%changelog
* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.1
+ Revision: 505281
- rebuild using %1.2 Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2-4mdv2010.0
+ Revision: 430538
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.2-3mdv2009.0
+ Revision: 241856
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdv2008.0
+ Revision: 56110
- new version


* Fri Dec 01 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdv2007.0
+ Revision: 89750
- Import perl-Snowball-Norwegian

* Wed Nov 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-3mdk
- changed name
- spec cleanup
- fix directory ownership
- %%mkrel
- rpmbuildupdate aware
- better summary
- better description
- better url

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-2mdk
- fix deps
- fix standard-dir-owned-by-package

