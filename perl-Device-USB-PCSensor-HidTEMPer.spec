#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		perl_version_stringify() %(perl -Mversion -le 'print version->parse(%1)->stringify' 2>/dev/null || ERROR)

%define		pdir	Device
%define		pver	%{perl_version_stringify %{version}}
%define		pver	0.0302
%define		pnam	USB-PCSensor-HidTEMPer
%include	/usr/lib/rpm/macros.perl
Summary:	Device::USB::PCSensor::HidTEMPer - Device overview
Name:		perl-Device-USB-PCSensor-HidTEMPer
Version:	0.03_02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MS/MSULLAND/Device-USB-PCSensor-HidTEMPer-%{pver}.tar.gz
# Source0-md5:	25b2f5dbb041282a7f17a66f1cd65054
# https://wwwx.cs.unc.edu/~hays/dev/bash/temper/temper_mon.pl
Source1:	temper_mon.pl
URL:		http://search.cpan.org/dist/Device-USB-PCSensor-HidTEMPer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Device::USB::Device) >= 0.29
BuildRequires:	perl-Device-USB >= 0.31
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a simplified interface to the HidTEMPer thermometers
created by PCSensor. It hides any problems recognizing the correct
objects to initialize and the dependency on Device::USB.

%prep
%setup -q -n %{pdir}-%{pnam}-%{pver}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{SOURCE1}  $RPM_BUILD_ROOT%{_bindir}/temper_mon
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/temper_mon
%dir %{perl_vendorlib}/Device/USB
%dir %{perl_vendorlib}/Device/USB/PCSensor
%{perl_vendorlib}/Device/USB/PCSensor/*.pm
%{perl_vendorlib}/Device/USB/PCSensor/HidTEMPer
%{_mandir}/man3/*
