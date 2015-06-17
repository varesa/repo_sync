Name:		repo_sync
Version:	1.0.0
Release:	1%{?dist}
BuildArch:	noarch
Summary:	Sync github and gitlab repositories
Group: 		System Environment/Base
License:	GPLv2+
URL:		https://github.com/varesa/repo_sync
Source0: 	%{name}-%{version}.tar.gz

Requires: python34u

%description

%prep
%autosetup

%build

%install
install -d 755 %{buildroot}/usr/share/repo_sync
find ./ -name "*.py" -exec install -m 644 {} %{buildroot}/usr/share/repo_sync/{} \;
install -m 644 gitlab_credentials.template %{buildroot}/usr/share/repo_sync/gitlab_credentials.template

install -m 755 repo_sync %{buildroot}/usr/bin/repo_sync

%files
/usr/*

%changelog