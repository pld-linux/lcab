Summary:	MS cab-files creator
Summary(pl):	Program tworz±cy pliki MS-cab
Name:		lcab
Version:	1.0b9
Release:	1
License:	distributable
Group:		Applications/Archiving
Source0:	http://www.geekshop.be/rien/lcab/files/%{name}-%{version}.tar.gz
# Source0-md5:	88c4b1159522ff1b44d805b88ed24b08
URL:		http://www.geekshop.be/rien/lcab/
Obsoletes:	cablinux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A little program that creates MS cabinet-files.

%description -l pl
Ma³y program tworz±cy pliki cabinet Microsoftu.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755, root, root) %{_bindir}/%{name}
