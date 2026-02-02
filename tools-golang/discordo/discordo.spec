%global commit 5f884cdf288d9950c9ef4bbced100458af89ca46
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:       discordo
Version:    20260202.%{short_commit}
Release:    1%{?dist}
Summary:    A lightweight, secure, and feature-rich Discord terminal (TUI) client.
License:    GPLv3
URL:        https://github.com/ayn2op/%{name}
Source:     %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildRequires: git-core
BuildRequires: go-md2man
BuildRequires: golang >= 1.25.3
BuildRequires: libX11-devel

Recommends: wl-clipboard

%description

%prep
%autosetup -n %{name}-%{commit}

%build
go build \
    -ldflags "-X main.version=%{version} -s -w" \
    -o _build/%{name} \
    ./cmd

go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
