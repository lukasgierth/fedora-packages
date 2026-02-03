%global debug_package %{nil}

Name:    bluetui
# renovate: datasource=github-releases depName=pythops/bluetui extractVersion=true
Version: 0.8.1
Release: 1%{?dist}
Summary: TUI for managing bluetooth on Linux
License: GPL-3.0-or-later
URL:     https://github.com/pythops/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

Requires: bluez

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

%install
install -Dpm 0755 target/release/bluetui -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc Readme.md
%{_bindir}/bluetui

%changelog
%autochangelog
