%global debug_package   %{nil}
%global import_path     github.com/syndtr/gocapability
%global gopath          %{_datadir}/gocode
%global commit          3454319be2ebde8481aa0804a801f4d07de705b5
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-syndtr-gocapability
Version:        0
Release:        0.5.git%{shortcommit}%{?dist}
Summary:        POSIX capability library for the Go programming language
License:        BSD
URL:            %{import_path}
Source0:        https://github.com/syndtr/gocapability/archive/%{commit}/gocapability-%{shortcommit}.tar.gz

%description
%{summary}

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        Source for POSIX capability for the Go programming language
%if 0%{?fedora} >= 19
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif
Provides:       golang(%{import_path}/capability) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages.


%prep
%setup -q -n gocapability-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av capability %{buildroot}/%{gopath}/src/%{import_path}/

%check
GOPATH=%{buildroot}/%{gopath} go test %{import_path}/capability

%files devel
%defattr(-,root,root,-)
%doc LICENSE
%dir %attr(755,root,root) %{gopath}/src/github.com
%dir %attr(755,root,root) %{gopath}/src/github.com/syndtr
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/capability
%{gopath}/src/%{import_path}/capability/*.go

%changelog
* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.git3454319
- exclusivearch for el6+

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.git3454319
- require golang as runtime dep

* Wed Nov 20 2013 Vincent Batts <vbatts@redhat.com> 0-0.3.git3454319
- typo

* Wed Nov 20 2013 Vincent Batts <vbatts@redhat.com> 0-0.2.git3454319
- clean up per code review (bz1032750)

* Wed Nov 20 2013 Vincent Batts <vbatts@redhat.com> 0-0.1.git3454319
- initial build
