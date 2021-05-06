%define debug_package %{nil}
%global shortname abs

Name:           %{shortname}-lang
Version:        2.4.2
Release:        1%{?dist}
Summary:        The ABS Programming Language
License:        MIT

URL:            https://www.abs-lang.org
Source0:        https://github.com/abs-lang/abs/archive/refs/tags/%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  make
BuildArch:      x86_64


%description
ABS is a programming language that works best when you're scripting on your
terminal.  It tries to combine the elegance of languages such as Python, or
Ruby, to the convenience of Bash.


%prep
%setup -q -n %{shortname}-%{version}
sed -r -i '/^build_simple/ {n; s/(-[[:lower:]]+)/-trimfile \1/}' Makefile


%build
make build_simple


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 builds/%{shortname} %{buildroot}/%{_bindir}/%{shortname}


%files
%license LICENSE
%{_bindir}/%{shortname}


%changelog
* Fri May 7 2021 mpatton
-
