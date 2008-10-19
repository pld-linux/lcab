Summary:	MS cab-files creator
Summary(pl.UTF-8):	Program tworzący pliki MS-cab
Name:		lcab
Version:	1.0b12
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://lcab.move-to-cork.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	9403e08f53fcf262e25641a9b900d4de
URL:		http://lcab.move-to-cork.com/
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	cablinux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LCAB is a small program that creates an uncompressed MS cabinet files.

%description -l pl.UTF-8
LCAB to mały program tworzący nieskompresowane pliki cabinet
Microsoftu.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install lcab.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755, root, root) %{_bindir}/%{name}
%{_mandir}/man1/lcab.1*
