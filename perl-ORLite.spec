%define upstream_name    ORLite
%define upstream_version 1.98

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Extremely light weight SQLite-specific ORM
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/ORLite-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(DBD::SQLite) >= 1.270
BuildRequires:	perl(DBI) >= 1.607
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Remove) >= 1.40
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp) >= 0.200.0
BuildRequires:	perl(Params::Util) >= 1.00
BuildRequires:	perl(Template::Tiny)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Script)

BuildArch:	noarch

%description
Extremely light weight SQLite-specific ORM

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Jul 09 2011 Shlomi Fish <shlomif@mandriva.org> 1.500.0-1mdv2011
+ Revision: 689373
- New version - 1.50

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.450.0-2
+ Revision: 653608
- rebuild for updated spec-helper

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.450.0-1mdv2011.0
+ Revision: 569946
- update to 1.45

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.440.0-1mdv2011.0
+ Revision: 561934
- update to 1.44

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.430.0-1mdv2011.0
+ Revision: 552480
- update to 1.43

* Tue Mar 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.420.0-1mdv2010.1
+ Revision: 521625
- update to 1.42

* Tue Mar 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1.410.0-1mdv2010.1
+ Revision: 517116
- update to 1.41

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2010.1
+ Revision: 499018
- update to 1.40

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.390.0-1mdv2010.1
+ Revision: 499001
- adding missing buildrequires:
- update to 1.39

* Wed Jan 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.340.0-1mdv2010.1
+ Revision: 497062
- adding missing buildrequires:
- update to 1.34

* Sun Jan 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.330.0-1mdv2010.1
+ Revision: 495432
- update to 1.33

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.320.0-1mdv2010.1
+ Revision: 491629
- update to 1.32

* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 1.310.0-1mdv2010.1
+ Revision: 485805
- update to 1.31

* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 1.280.0-1mdv2010.0
+ Revision: 450010
- update buildrequires:
- update to 1.28

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.250.0-1mdv2010.0
+ Revision: 416983
- update to 1.25

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-1mdv2010.0
+ Revision: 396880
- using %%perl_convert_version
- fixed license field

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.23-2mdv2010.0
+ Revision: 396753
- rebuilding to get new automatic provides extraction

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2010.0
+ Revision: 389799
- update to new version 1.23

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2010.0
+ Revision: 384044
- update to new version 1.22

* Sat Feb 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2009.1
+ Revision: 345921
- update to new version 1.20

* Sat Jan 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.18-1mdv2009.1
+ Revision: 330589
- update to new version 1.18

* Mon Jan 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.17-1mdv2009.1
+ Revision: 325079
- update to new version 1.17

* Tue Oct 21 2008 Jérôme Quelin <jquelin@mandriva.org> 0.15-1mdv2009.1
+ Revision: 296230
- update to new version 0.15

* Sat Aug 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10-1mdv2009.0
+ Revision: 277675
- import perl-ORLite



