%global debug_package %{nil}

Name:       gophertube
# renovate: datasource=github-releases depName=KrishnaSSH/gophertube extractVersion=true
Version:    2.8.0
Release:    1%{?dist}
Summary:    A modern terminal user interface for searching and watching YouTube videos using mpv and chafa
License:    GPL-3.0-or-later
URL:        https://github.com/KrishnaSSH/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.23.2

Requires: chafa
Requires: fzf
Requires: mpv
Requires: yt-dlp

%description

%prep
%autosetup -n %{name}-%{version}

%build
go build \
    -ldflags "-X main.version=%{version} -s -w" \
    -o _build/%{name}
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
