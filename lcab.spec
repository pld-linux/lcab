Summary:	MS cab-files creator
Summary(pl):	Program tworz±cy pliki MS-cab
Name:		lcab
Version:	1.0b10
Release:	3
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.geekshop.be/rien/lcab/files/%{name}-%{version}.tar.gz
# Source0-md5:	8094f3b6e2211ff223f6b9e01d83db3c
URL:		http://www.geekshop.be/rien/lcab/
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	cablinux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A little program that creates MS cabinet-files.

%description -l pl
Ma³y program tworz±cy pliki cabinet Microsoftu.

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
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755, root, root) %{_bindir}/%{name}
