%define upstream_name    Catalyst-Plugin-Session-Store-Cache
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Store sessions using a Catalyst::Plugin::Cache
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Catalyst-Plugin-Session-Store-Cache
Source0:	https://cpan.metacpan.org/authors/id/L/LB/LBR/Catalyst-Plugin-Session-Store-Cache-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Plugin::Session)
BuildArch:	noarch

%description
This plugin will store your session data in whatever cache module you have
configured.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

