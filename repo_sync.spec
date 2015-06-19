Name:		repo_sync
Version:	1.0.0
Release:	1%{?dist}
BuildArch:	noarch
Summary:	Sync github and gitlab repositories
Group: 		System Environment/Base
License:	GPLv2+
URL:		https://github.com/varesa/repo_sync
Source0: 	%{name}-%{version}.tar.gz

Requires: python34u git

%description

%prep
%autosetup

%build

%install
install -d -m 755 %{buildroot}/usr/share/repo_sync
find ./ -name "*.py" -exec install -m 644 {} %{buildroot}/usr/share/repo_sync/{} \;

install -d %{buildroot}/usr/bin/
install -m 755 repo_sync %{buildroot}/usr/bin/repo_sync

%files
/usr/bin/*
/usr/share/*

%changelog