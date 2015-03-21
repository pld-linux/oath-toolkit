Summary:	OATH Toolkit - easily build one-time password authentication systems
Summary(pl.UTF-8):	OATH Toolkit - łatwe tworzenie systemów uwierzytelniania z jednorazowymi hasłami
Name:		oath-toolkit
Version:	2.4.1
Release:	3
License:	LGPL v2.1+ (libraries), GPL v3+ (utilities and PAM module)
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/oath-toolkit/%{name}-%{version}.tar.gz
# Source0-md5:	951bafd1d86e6013903c10be3b6623bb
URL:		http://www.nongnu.org/oath-toolkit/
BuildRequires:	gtk-doc >= 1.1
BuildRequires:	help2man
BuildRequires:	libxml2-devel >= 2
BuildRequires:	pam-devel
BuildRequires:	xmlsec1-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OATH Toolkit makes it easy to build one-time password
authentication systems. It contains shared libraries, command line
tools and a PAM module. Supported technologies include the event-based
HOTP algorithm (RFC4226) and the time-based TOTP algorithm (RFC6238).
OATH stands for Open AuTHentication, which is the organization that
specify the algorithms. For managing secret key files, the Portable
Symmetric Key Container (PSKC) format described in RFC6030 is
supported.

%description -l pl.UTF-8
OATH Toolkit ułatwia tworzenie systemów uwierzytelniania z
jednorazowymi hasłami. Zawiera biblioteki współdzielone, narzędzia
działające z linii poleceń oraz moduł PAM. Obsługiwane techniki
obejmują oparty na zdarzeniach algorytm HOTP (RFC 4226) oraz oparty na
czasie algorytm TOTP (RFC 6238). OATH to skrót od Open AuTHentication
- nazwy organizacji opisującej algorytmy. W celu zarządzania kluczami
  obsługiwany jest format PSKC (Portable Symmetric Key Container),
  opisany w RFC 6030.

%package devel
Summary:	Header files for OATH libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek OATH
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2-devel >= 2
Requires:	xmlsec1-devel

%description devel
Header files for OATH libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek OATH.

%package static
Summary:	Static OATH libraries
Summary(pl.UTF-8):	Statyczne biblioteki OATH
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OATH libraries.

%description static -l pl.UTF-8
Statyczne biblioteki OATH.

%package apidocs
Summary:	OATH API documentation
Summary(pl.UTF-8):	Dokumentacja API bibliotek OATH
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for OATH libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek OATH.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir} \
	--with-pam-dir=/%{_lib}/security
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# lib*.la kept - libpskc is missing .private dependencies

%{__rm} $RPM_BUILD_ROOT/%{_lib}/security/pam_*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains just licensing notes
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/oathtool
%attr(755,root,root) %{_bindir}/pskctool
%attr(755,root,root) %{_libdir}/liboath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboath.so.0
%attr(755,root,root) %{_libdir}/libpskc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpskc.so.0
%attr(755,root,root) /%{_lib}/security/pam_oath.so
%{_datadir}/xml/pskc
%{_mandir}/man1/oathtool.1*
%{_mandir}/man1/pskctool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboath.so
%attr(755,root,root) %{_libdir}/libpskc.so
%{_libdir}/liboath.la
%{_libdir}/libpskc.la
%{_includedir}/liboath
%{_includedir}/pskc
%{_pkgconfigdir}/liboath.pc
%{_pkgconfigdir}/libpskc.pc
%{_mandir}/man3/oath_*.3*
%{_mandir}/man3/pskc_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/liboath.a
%{_libdir}/libpskc.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/liboath
%{_gtkdocdir}/libpskc
