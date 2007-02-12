Summary:	TCP proxy with load balancing
Summary(pl.UTF-8):   Proxy TCP z load balancingiem
Name:		balance
Version:	3.35
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.inlab.de/%{name}-%{version}.tar.gz
# Source0-md5:	771f8523f7a4ee119461e7f71f8a275f
URL:		http://www.inlab.de/balance.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Balance is our suprisingly successful load balancing solution being a
simple but powerful generic TCP proxy with round robin load balancing
and failover mechanisms. Its behaviour can be controlled at runtime
using a simple command line syntax.

%description -l pl.UTF-8
Balance jest prostym, ale bardzo skutecznym proxy TCP z load
balancingiem. Jego zachowanie w czasie działania może być kontrolowane
z linii poleceń, przy użyciu prostej składni.

%prep
%setup -q

%build
%{__make} balance \
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
