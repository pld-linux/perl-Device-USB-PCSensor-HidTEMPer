#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Device
%define		pnam	USB-PCSensor-HidTEMPer
%include	/usr/lib/rpm/macros.perl
Summary:	Device::USB::PCSensor::HidTEMPer - Device overview
Name:		perl-Device-USB-PCSensor-HidTEMPer
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MS/MSULLAND/Device-USB-PCSensor-HidTEMPer-%{version}.tar.gz
# Source0-md5:	fbb21e800581be5aab4b8893bcde3393
URL:		http://search.cpan.org/dist/Device-USB-PCSensor-HidTEMPer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Device-USB >= 0.31
BuildRequires:	perl(Device::USB::Device) >= 0.29
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a simplified interface to the HidTEMPer thermometers
created by PCSensor. It hides any problems recognizing the correct
objects to initialize and the dependency on Device::USB.

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
%dir %{perl_vendorlib}/Device/USB
%dir %{perl_vendorlib}/Device/USB/PCSensor
%{perl_vendorlib}/Device/USB/PCSensor/*.pm
%{perl_vendorlib}/Device/USB/PCSensor/HidTEMPer
%{_mandir}/man3/*
