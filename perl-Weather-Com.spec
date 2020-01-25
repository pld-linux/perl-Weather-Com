#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Weather
%define		pnam	Com
Summary:	Fetching weather information from weather.com
Summary(pl.UTF-8):	Pobieranie informacji pogodowych z weather.com
Name:		perl-Weather-Com
Version:	0.5.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Weather/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b4432b0e87f9dd53cb06979b2c8a6b1a
URL:		http://search.cpan.org/dist/Weather-Com/
BuildRequires:	perl-Time-Format >= 1.0
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fetching weather information from weather.com.

%description -l pl.UTF-8
Pobieranie informacji pogodowych z weather.com.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Weather/Com.pm
%dir %{perl_vendorlib}/Weather/Com
%{perl_vendorlib}/Weather/Com/*.pm
%dir %{perl_vendorlib}/Weather/Com/L10N
%{perl_vendorlib}/Weather/Com/L10N/*.pm
%{_mandir}/man3/*
