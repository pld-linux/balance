Summary:	TCP proxy with load balancing
Summary(pl):	TCP proxy z load balancingiem
Name:		balance
Version:	3.19
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.inlab.de/%{name}-%{version}.tar.gz
# Source0-md5:	7791586953fade0592d0cac215218167
URL:		http://www.inlab.de/balance.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Balance is our suprisingly successful load balancing solution being a
simple but powerful generic tcp proxy with round robin load balancing
and failover mechanisms. Its behaviour can be controlled at runtime
using a simple command line syntax.

%description -l pl
Balance jest prostym, ale bardzo skutecznym tcp proxy z load
balancingiem. Jego zachowanie w czasie dzia³ania mo¿e byæ kontrolowane
z linii poleceñ, przy u¿yciu prostej sk³adni.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/var/run/balance,%{_mandir}/man1}

install balance $RPM_BUILD_ROOT%{_sbindir}
install balance.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %attr(700,root,root) /var/run/balance
%attr(755,root,root) %{_sbindir}/balance
%{_mandir}/man1/*
