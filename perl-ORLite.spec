%define realname   ORLite
%define version    1.20
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Extremely light weight SQLite-specific ORM  
Source:     http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%realname-%version.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Params::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::Spec)

BuildArch: noarch

%description
Extremely light weight SQLite-specific ORM  


%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*