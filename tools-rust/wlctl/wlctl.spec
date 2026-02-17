%global debug_package %{nil}

Name:    wlctl
# renovate: datasource=github-releases depName=aashish-thapa/wlctl extractVersion=true
Version: 0.1.5
Release: 1%{?dist}
Summary: TUI for managing wifi on Linux with Network Manager. Forked from impala
License: GPL-3.0-or-later
URL:     https://github.com/aashish-thapa/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

Requires: NetworkManager

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc Readme.md
%{_bindir}/%{name}

%changelog
%autochangelog
