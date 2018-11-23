#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Email-MessageID
Version  : 1.406
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-MessageID-1.406.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-MessageID-1.406.tar.gz
Summary  : 'Generate world unique message-ids.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Email-MessageID-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Email-MessageID,
version 1.406:
Generate world unique message-ids.

%package dev
Summary: dev components for the perl-Email-MessageID package.
Group: Development
Provides: perl-Email-MessageID-devel = %{version}-%{release}

%description dev
dev components for the perl-Email-MessageID package.


%package license
Summary: license components for the perl-Email-MessageID package.
Group: Default

%description license
license components for the perl-Email-MessageID package.


%prep
%setup -q -n Email-MessageID-1.406

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Email-MessageID
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Email-MessageID/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Email/MessageID.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Email::MessageID.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Email-MessageID/LICENSE
